//
//  InternetUtilClass.swift
//  Shipit
//
//  Created by mac on 24/09/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit

let NETWORK_ERROR_MSG : String  =  "Nenhuma conexão com a Internet. Você não tem conexão com a internet."

class InternetUtilClass{
    
    class var sharedInstance: InternetUtilClass {
        
        struct Static {
            
            static let instance: InternetUtilClass = InternetUtilClass()
            static var reachability: Reachability? = Reachability.forInternetConnection()
        }
        
        return Static.instance
    }
    
    func hasConnectivity() -> Bool {
        let reachability: Reachability = Reachability.forInternetConnection()
        let networkStatus: Int = reachability.currentReachabilityStatus().rawValue
        return networkStatus != 0
    }
    
    
}
