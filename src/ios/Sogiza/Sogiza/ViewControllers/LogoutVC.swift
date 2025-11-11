//
//  LogoutVC.swift
//  Sogiza
//
//  Created by mac on 26/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit

class LogoutVC: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        let domain = Bundle.main.bundleIdentifier!
        UserDefaults.standard.removePersistentDomain(forName: domain)
        UserDefaults.standard.synchronize()
        Switcher.updateRootVC()
    }
}
