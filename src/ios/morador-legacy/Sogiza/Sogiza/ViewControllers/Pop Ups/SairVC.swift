//
//  SairVC.swift
//  Sogiza
//
//  Created by mac on 18/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit

protocol LogoutProtocol: class {
    func didTappedOnLogout()
}

class SairVC: UIViewController {

    weak var delegate: LogoutProtocol?
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    @IBAction func btnSim(_ sender: UIButton) {
        delegate?.didTappedOnLogout()
    }
    
    @IBAction func btnCancelar(_ sender: UIButton) {
        dismiss(animated: true, completion: nil)
    }
    
}
