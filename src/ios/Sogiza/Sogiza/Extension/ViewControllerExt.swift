//
//  ViewControllerExt.swift
//  WeCare
//
//  Created by mac on 29/09/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit

extension UIViewController {
    
    func setNavigationBarItem(LeftTitle:String, RightTitle:String) {
        if LeftTitle != "" {
            self.addLeftBarButtonWithImage(UIImage(named: LeftTitle)!)
        }
        if RightTitle != "" {
            self.addRightBarButtonWithImage(UIImage(named: RightTitle)!)
        }
        self.setNavigationbarTextColor(color: UIColor.black)
    }
    
    func removeNavigationBarItem() {
        self.navigationItem.setHidesBackButton(true, animated:true);
        self.navigationItem.leftBarButtonItem = nil
        self.navigationItem.rightBarButtonItem = nil
    }
    
    public func addLeftBarButtonWithImage(_ buttonImage: UIImage) {
        let leftButton = UIBarButtonItem(image: buttonImage, style: .plain, target: self, action: #selector(self.leftClick))
        navigationItem.leftBarButtonItem = leftButton
    }
    
    public func addRightBarButtonWithImage(_ buttonImage: UIImage) {
        let rightButton = UIBarButtonItem(image: buttonImage, style: .plain, target: self, action: #selector(self.rightClick))
        navigationItem.rightBarButtonItem = rightButton
//        let rightButton: UIBarButtonItem = UIBarButtonItem(title: title, style: UIBarButtonItemStyle.plain, target: self, action: #selector(self.toggleRight))
//        navigationItem.rightBarButtonItem = rightButton
    }
    
    public func setNavigationbarImage() {
        self.navigationController?.navigationBar.setBackgroundImage(UIImage(named: "Rectangle-34")?.resizableImage(withCapInsets: UIEdgeInsets.zero, resizingMode: .stretch), for: .default)
    }
    
    public func setNavigationbarTextColor(color: UIColor) {
        navigationController?.navigationBar.tintColor = .black
        navigationController?.navigationBar.titleTextAttributes = [.foregroundColor: color]
    }
    
    public func leftClick() {
        //navigationController?.popViewController(animated: true)
    }
    
    public func rightClick() {
        
    }
    
    func hexStringToUIColor (hex:String) -> UIColor {
        var cString:String = hex.trimmingCharacters(in: .whitespacesAndNewlines).uppercased()
        
        if (cString.hasPrefix("#")) {
            cString.remove(at: cString.startIndex)
        }
        
        if cString.count != 6 {
            return UIColor.gray
        }
        
        var rgbValue: UInt64 = 0
        Scanner(string: cString).scanHexInt64(&rgbValue)
        
        return UIColor(
            red: CGFloat((rgbValue & 0xFF0000) >> 16) / 255.0,
            green: CGFloat((rgbValue & 0x00FF00) >> 8) / 255.0,
            blue: CGFloat(rgbValue & 0x0000FF) / 255.0,
            alpha: CGFloat(1.0)
        )
    }
    
    func showProgressBar() {
        let spinnerActivity = MBProgressHUD.showAdded(to: self.view, animated: true)
        spinnerActivity.label.text = "Loading"
        spinnerActivity.detailsLabel.text = "Please Wait!!"
        spinnerActivity.isUserInteractionEnabled = false
    }
    
    func hideProgressBar() {
        MBProgressHUD.hide(for: self.view, animated: true)
    }
    
    func alert(alertmessage: String) {
        let alert = UIAlertController(title: APP_NAME, message: alertmessage, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: { action in
            switch action.style{
            case .default:
                print("default")
                
            case .cancel:
                print("cancel")
                
            case .destructive:
                print("destructive")
            }
        }
            )
        )
        self.present(alert, animated: true, completion: nil)
    }
}
