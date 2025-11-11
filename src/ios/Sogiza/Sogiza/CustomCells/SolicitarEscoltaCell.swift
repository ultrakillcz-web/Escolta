//
//  SolicitarEscoltaCell.swift
//  Sogiza
//
//  Created by mac on 18/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit

@objc protocol requestProtocol : class {
    func didTappedOnRequest(_ tag: Int)
}

class SolicitarEscoltaCell: UITableViewCell {

    @IBOutlet weak var lblName: UILabel!
    @IBOutlet weak var lblAddress: UILabel!
    @IBOutlet weak var lblMobile: UILabel!
    
    @IBOutlet weak var btnRequest: UIButton!
    weak var delegate: requestProtocol?
    
    override func awakeFromNib() {
        super.awakeFromNib()
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)
    }

    @IBAction func btnRequest(_ sender: UIButton) {
        delegate?.didTappedOnRequest(sender.tag)
    }
}
