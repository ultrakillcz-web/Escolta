//
//  LoginVC.swift
//  Sogiza
//
//  Created by mac on 18/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit
import SwiftyJSON
import InputMask

class LoginVC: UIViewController {
    
    @IBOutlet weak var txtMobile: UITextField!
    @IBOutlet weak var txtPassword: UITextField!
    @IBOutlet var listnerPhoneNo: PolyMaskTextFieldDelegate!
    @IBOutlet var listerPassword: PolyMaskTextFieldDelegate!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        listnerPhoneNo.affineFormats    = ["[00000000000]"]
        listerPassword.affineFormats    = ["[0000]"]
    }
    
    open func textField(
        _ textField: UITextField,
        didFillMandatoryCharacters complete: Bool,
        didExtractValue value: String
        ) {
        print(value)
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        navigationController?.navigationBar.isHidden = true
    }
    
    @IBAction func btnLogin(_ sender: UIButton) {
        if isValidInput() {
            login()
        }
    }

    func inputDictLogin() -> [String:AnyObject] {
        var dict : [String:AnyObject] = [:]
        dict["mobile"]              =   txtMobile.text as AnyObject
        dict["password"]            =   txtPassword.text as AnyObject
        dict["type"]                =   "USER" as AnyObject
        dict["lat"]                 =   "" as AnyObject
        dict["lon"]                 =   "" as AnyObject
        dict["ios_register_id"]     =   "" as AnyObject
        return dict
    }
    
    func login() {
        showProgressBar()
        let paramsDict = self.inputDictLogin()
        print(paramsDict)
        CommunicationManeger.callPostService(apiUrl: BASE_URL + END_POINT_LOGIN, parameters: paramsDict, parentViewController: self,
                                             successBlock: { (response : AnyObject,message : String) in
                                                self.parseDataLogin(apiResponse: response, apiMessage: message)
        },
                                             failureBlock: { (error : Error) in
                                                Utility.showAlertMessage(withTitle: EMPTY_STRING, message: (error.localizedDescription), delegate: nil,parentViewController: self)
        })
    }
    
    func parseDataLogin(apiResponse : AnyObject, apiMessage : String) {
        // Bounce back to the main thread to update the UI
        DispatchQueue.main.async {
            let swiftyJsonVar = JSON(apiResponse)
            if(swiftyJsonVar["status"] == "1") {
                print(swiftyJsonVar["result"])
                UserDefaults.standard.set(true, forKey: "status")
                UserDefaults.standard.set(swiftyJsonVar["result"]["id"].string, forKey: "user_id")
                UserDefaults.standard.set(swiftyJsonVar["result"]["username"].string, forKey: "username")
                UserDefaults.standard.set(swiftyJsonVar["result"]["type"].string, forKey: "user_type")
                Switcher.updateRootVC()
            } else {
                UserDefaults.standard.set(false, forKey: "status")
                UserDefaults.standard.set("", forKey: "user_id")
                UserDefaults.standard.set("", forKey: "username")
                UserDefaults.standard.set("", forKey: "user_type")
                self.txtPassword.text = ""
                let message = swiftyJsonVar["result"].string
                self.alert(alertmessage: message!)
            }
            self.hideProgressBar()
        }
    }
    
    func isValidInput() -> Bool {
        var isValid : Bool = true;
        var errorMessage : String = ""
        if (self.txtMobile.text?.isEmpty)! {
            isValid = false
            errorMessage = "Campo obrigatório"
            txtMobile.becomeFirstResponder()
        }
        else if (!Utility.isValidMobileNumber(txtMobile.text!)){
            isValid = false
            errorMessage = "Campo obrigatório"
            txtPassword.text = ""
            txtMobile.text = ""
            txtMobile.becomeFirstResponder()
        }
        else if (self.txtPassword.text?.isEmpty)!{
            isValid = false
            errorMessage = "Campo obrigatório"
            txtPassword.becomeFirstResponder()
        }
        else if (!Utility.isValidPassword(txtPassword.text!)) {
            isValid = false
            txtPassword.text = ""
            errorMessage = "Campo obrigatório"
            txtPassword.becomeFirstResponder()
        }
        if (isValid == false) {
            Utility.showAlertMessage(withTitle: EMPTY_STRING,
                                     message: errorMessage,
                                     delegate: nil,
                                     parentViewController: self)
        }
        return isValid
    }
}
