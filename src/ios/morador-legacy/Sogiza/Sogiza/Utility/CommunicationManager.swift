//
//  CommunicationManager.swift
//  Shipit
//
//  Created by mac on 24/09/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import Foundation
import Alamofire
import SwiftyJSON

class CommunicationManeger {
    
    //MARK: - POST API Request
    class func callPostService(apiUrl urlString: String, parameters params : [String: AnyObject]?,  parentViewController parentVC: UIViewController, successBlock success : @escaping ( _ responseData : AnyObject, _  message: String) -> Void, failureBlock failure: @escaping (_ error: Error) -> Void) {
        
        if Utility.checkNetworkConnectivityWithDisplayAlert(isShowAlert: true) {
            let manager = Alamofire.SessionManager.default
            manager.session.configuration.timeoutIntervalForRequest = 120
            manager.request(urlString, method: .post, parameters: params)
                .responseJSON {
                    response in
                    switch (response.result) {
                    case .success:
                        if((response.result.value) != nil) {
                            success(response.result.value as AnyObject, "Successfull")
                        }
                        break
                    case .failure(let error):
                        print(error)
                        if error._code == NSURLErrorTimedOut {
                            //HANDLE TIMEOUT HERE
                            print(error.localizedDescription)
                            failure(error)
                        } else {
                            print("\n\nAuth request failed with error:\n \(error)")
                            failure(error)
                        }
                        break
                    }
            }
        } else {
            parentVC.hideProgressBar();
            Utility.showAlertMessage(withTitle: EMPTY_STRING, message: NETWORK_ERROR_MSG, delegate: nil, parentViewController: parentVC)
        }
    }
    
    //MARK: - Multipart API Request for upload multiple photos
    class func uploadImagesAndData(apiUrl urlString: String, params:[String : String]?,imageParam: [String : UIImage?]?,  parentViewController parentVC: UIViewController, successBlock success : @escaping ( _ responseData : AnyObject, _  message: String) -> Void, failureBlock failure: @escaping (_ error: Error) -> Void){
        if Utility.checkNetworkConnectivityWithDisplayAlert(isShowAlert: true) {
            let headers: HTTPHeaders = [
                /* "Authorization": "your_access_token",  in case you need authorization header */
               // "Content-type": "multipart/form-data"
                "Content-Type": "application/json"
            ]
            
            Alamofire.upload(multipartFormData: {multipartFormData in
                for (key, value) in params! {
                    if let data = value.data(using: String.Encoding(rawValue:  String.Encoding.utf8.rawValue)) {
                        //print("Filed Name : \(key), Value :\(value)")
                        multipartFormData.append(data, withName: key)
                    }
                    
                }
                
                for (key, image) in imageParam! {
                    if let imageData = UIImageJPEGRepresentation(image!, 0.5) {
                        print(imageData)
                        //print("File Name : \(key).jpg")
                        multipartFormData.append(imageData, withName: key as String, fileName: "\(key).jpg", mimeType: "image/jpeg")
                    }
                }
            },
                             to: urlString, headers: headers, encodingCompletion: { encodingResult in
                                switch encodingResult {
                                case .success(let upload, _, _):
                                    upload
                                        .uploadProgress(closure: { (progress) in
                                            //print("Progress : \(progress)")
                                        })
                                        .validate()
                                        .responseJSON { response in
                                            print(response)
                                            if(response.result.isSuccess) {
                                                success(response.result.value as AnyObject,  "Successfull")
                                            }
                                            else {
                                                failure(response.result.error! as Error)
                                            }
                                    }
                                case .failure(let error):
                                    print(error)
                                    if error._code == NSURLErrorTimedOut {
                                        //HANDLE TIMEOUT HERE
                                        failure(error)
                                    } else {
                                        failure(error)
                                    }
                                    break
                                }
            })
        } else {
            parentVC.hideProgressBar();
            Utility.showAlertMessage(withTitle: EMPTY_STRING, message: NETWORK_ERROR_MSG, delegate: nil, parentViewController: parentVC)
        }
    }
}
