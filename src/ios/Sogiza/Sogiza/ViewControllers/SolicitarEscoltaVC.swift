//
//  SolicitarEscoltaVC.swift
//  Sogiza
//
//  Created by mac on 18/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit
import SwiftyJSON
import CoreLocation

class SolicitarEscoltaVC: UIViewController, requestProtocol, LocationManagerDelegate {
    
    var responseDict: [JSON]!
    var escortId:String = ""
    var CURRENT_LAT = ""
    var CURRENT_LON = ""
    var isValidLocation:Bool = true
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.navigationItem.title = "SOGIZA"
        LocationManager.sharedInstance.delegate = self
        LocationManager.sharedInstance.startUpdatingLocation()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        self.navigationController?.navigationBar.isHidden = false
        self.setNavigationBarItem(LeftTitle: "", RightTitle: "logout")
    }
    
    func didTappedOnRequest(_ tag: Int) {
        escortId = responseDict[tag]["id"].string!
        acceptRequest()
    }
    
    // MARK: LocationService Delegate
    func tracingLocation(currentLocation: CLLocation) {
        if currentLocation != nil {
            if isValidLocation {
                CURRENT_LAT = String(currentLocation.coordinate.latitude)
                CURRENT_LON = String(currentLocation.coordinate.longitude)
            }
        }
    }
    
    func tracingLocationDidFailWithError(error: NSError) {
        print("tracing Location Error : \(error.description)")
    }
    
    func inputDictAcceptRequest() -> [String:AnyObject] {
        var dict : [String:AnyObject] = [:]
        dict["user_id"]     =   UserDefaults.standard.string(forKey: "user_id") as AnyObject
        dict["escort_id"]   =   escortId as AnyObject
        dict["lat"]         =   CURRENT_LAT as AnyObject
        dict["lon"]         =   CURRENT_LON as AnyObject
        return dict
    }
    
    func acceptRequest() {
        isValidLocation = false
        showProgressBar()
        let inputDict = self.inputDictAcceptRequest()
        CommunicationManeger.callPostService(apiUrl: BASE_URL + END_POINT_ACCEPT_REQUEST, parameters: inputDict, parentViewController: self,
                                             successBlock: { (response : AnyObject,message : String) in
                                                self.parseDataAcceptRequest(apiResponse: response, apiMessage: message)
        },
                                             failureBlock: { (error : Error) in
                                                Utility.showAlertMessage(withTitle: EMPTY_STRING, message: (error.localizedDescription), delegate: nil,parentViewController: self)
        })
    }
    
    func parseDataAcceptRequest(apiResponse : AnyObject, apiMessage : String) {
        // Bounce back to the main thread to update the UI
        DispatchQueue.main.async {
            let swiftyJsonVar = JSON(apiResponse)
            print(swiftyJsonVar)
            if(swiftyJsonVar["status"] == "1") {
                self.alert(alertmessage: "")
            } else {
                self.alert(alertmessage: "Não ha escoltas disponiveis")
            }
            self.hideProgressBar()
        }
    }
}

extension SolicitarEscoltaVC: UITableViewDataSource {
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        if let _ = responseDict {
            return responseDict.count
        }
        return 0
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell:SolicitarEscoltaCell = tableView.dequeueReusableCell(withIdentifier: "SolicitarEscoltaCell", for: indexPath) as! SolicitarEscoltaCell
        if let response = responseDict {
            let object = response[indexPath.row]
            cell.lblName.text = object["username"].string!
            cell.lblMobile.text = object["mobile"].string!
            cell.lblAddress.text = object["street"].string!
            cell.btnRequest.tag = indexPath.row
            cell.delegate = self
        }
        return cell
    }
}
