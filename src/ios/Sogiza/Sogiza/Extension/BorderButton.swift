//
//  BorderButton.swift
//  WeCare
//
//  Created by mac on 08/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit

class ButtonCornerRound: UIButton {

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
        //        self.borderStyle = .none
        self.layer.cornerRadius = self.frame.height/2
       // self.layer.borderWidth = 1.0
     //   self.layer.borderColor =
        self.layer.masksToBounds = false
        self.layer.backgroundColor = UIColor.init(colorLiteralRed: 131/256, green: 24/256, blue: 95/256, alpha: 1).cgColor
        
        self.layer.sublayerTransform = CATransform3DMakeTranslation(0, 0, 0)
    }

}


class BorderButton: UIButton {
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
        self.layer.cornerRadius = 5
        self.layer.borderWidth = 0.5
        self.layer.borderColor = UIColor.init(colorLiteralRed: 241/256, green: 241/256, blue: 241/256, alpha: 1).cgColor
        
        self.layer.shadowColor = UIColor.lightGray.cgColor
        self.layer.shadowOffset = CGSize(width: 0, height: 0.5)
        self.layer.shadowRadius = 1
        self.layer.shadowOpacity = 1.0
        
        self.layer.masksToBounds = false
        // set backgroundColor in order to cover the shadow inside the bounds
        self.layer.backgroundColor = UIColor.white.cgColor
        
        self.layer.sublayerTransform = CATransform3DMakeTranslation(10, 0, 0)
    }
}
