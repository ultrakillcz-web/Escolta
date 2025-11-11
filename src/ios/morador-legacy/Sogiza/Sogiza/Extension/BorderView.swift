//
//  BorderView.swift
//  WeCare
//
//  Created by mac on 09/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit

class BorderView: UIView {

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
        self.layer.cornerRadius = 10
        self.layer.borderWidth = 1.5
        self.layer.borderColor = UIColor.init(colorLiteralRed: 241/256, green: 241/256, blue: 241/256, alpha: 1).cgColor
        
        self.layer.shadowColor = UIColor.lightGray.cgColor
        self.layer.shadowOffset = CGSize(width: 0, height: 0.5)
        self.layer.shadowRadius = 2
        self.layer.shadowOpacity = 1.0
        
        self.layer.masksToBounds = false
        // set backgroundColor in order to cover the shadow inside the bounds
        self.layer.backgroundColor = UIColor.white.cgColor
        
//        self.layer.sublayerTransform = CATransform3DMakeTranslation(0, 0, 0)
    }
}
