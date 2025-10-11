//
//  HomeVC.swift
//  Sogiza
//
//  Created by mac on 18/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit
import GoogleMaps
import SwiftyJSON
import CoreLocation

class HomeVC: UIViewController, GMSMapViewDelegate, LocationManagerDelegate, LogoutProtocol {
    
    @IBOutlet weak var mapView: GMSMapView!
    
    var responseDict: [JSON]!
    var CURRENT_LAT = ""
    var CURRENT_LON = ""
    var isValidLocation:Bool = true
    var centerMapCoordinate:CLLocationCoordinate2D!
    
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
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
    }
    
    func mapView(_ mapView: GMSMapView, didTapAt coordinate: CLLocationCoordinate2D) {
        print("You tapped at \(coordinate.latitude), \(coordinate.longitude)")
    }
    
//    func mapView(_ mapView: GMSMapView, didTap marker: GMSMarker) -> Bool {
//        print("You tapped : \(marker.position.latitude),\(marker.position.longitude)")
//        return true
//    }
    
    /* set a custom Info Window */
    func mapView(_ mapView: GMSMapView, markerInfoWindow marker: GMSMarker) -> UIView? {
        let markerIndex = marker.title!
        print(markerIndex)
        print(responseDict)
        let view = UIView(frame: CGRect.init(x: 0, y: 0, width: 200, height: 70))
        view.backgroundColor = UIColor.white
        view.layer.cornerRadius = 6
        
        let lbl1 = UILabel(frame: CGRect.init(x: 8, y: 8, width: view.frame.size.width - 16, height: 15))
        lbl1.text = marker.title
        view.addSubview(lbl1)
        
        let lbl2 = UILabel(frame: CGRect.init(x: lbl1.frame.origin.x, y: lbl1.frame.origin.y + lbl1.frame.size.height + 3, width: view.frame.size.width - 16, height: 15))
        lbl2.text = "I am a custom info window."
//        lbl2.font = UIFont.systemFont(ofSize: 14, weight: .light)
        view.addSubview(lbl2)
        return view
    }
    
    // MARK: LocationService Delegate
    func tracingLocation(currentLocation: CLLocation) {
        print(currentLocation)
        if currentLocation != nil {
            if isValidLocation {
                CURRENT_LAT = String(currentLocation.coordinate.latitude)
                CURRENT_LON = String(currentLocation.coordinate.longitude)
                print(CURRENT_LAT)
                print(CURRENT_LON)
                getNearByUsers()
            }
        }
    }
    
    func tracingLocationDidFailWithError(error: NSError) {
        print("tracing Location Error : \(error.description)")
    }
    
    func inputDictNearByUsers() -> [String:AnyObject] {
        var dict : [String:AnyObject] = [:]
        dict["lat"] =   CURRENT_LAT as AnyObject
        dict["lon"] =   CURRENT_LON as AnyObject
        return dict
    }
    
    func getNearByUsers() {
        isValidLocation = false
        showProgressBar()
        let inputDict = self.inputDictNearByUsers()
        print(inputDict)
        CommunicationManeger.callPostService(apiUrl: BASE_URL + END_POINT_GET_GUARDS, parameters: inputDict, parentViewController: self,
                                             successBlock: { (response : AnyObject,message : String) in
                                                self.parseDataNearByUsers(apiResponse: response, apiMessage: message)
        },
                                             failureBlock: { (error : Error) in
                                                Utility.showAlertMessage(withTitle: EMPTY_STRING, message: (error.localizedDescription), delegate: nil,parentViewController: self)
        })
    }
    
    func parseDataNearByUsers(apiResponse : AnyObject, apiMessage : String) {
        // Bounce back to the main thread to update the UI
        DispatchQueue.main.async {
            let swiftyJsonVar = JSON(apiResponse)
            if(swiftyJsonVar["status"] == "1") {
                // Getting an array of string from a JSON Array
                self.responseDict =  swiftyJsonVar["result"].arrayValue
                self.drawMap()
            } else {
                let message = swiftyJsonVar["result"].string
                self.alert(alertmessage: message!)
            }
            self.hideProgressBar()
        }
    }
    
    func drawMap() {
        
        let camera = GMSCameraPosition.camera(withLatitude: 22.703065308742225, longitude: 75.87223422713578, zoom: 14.0)
        mapView.camera = camera
        mapView.isMyLocationEnabled = true
        mapView.delegate = self
        
        print(self.responseDict)
        
        for val in responseDict {
            let lat = Double(val["lat"].string!)
            let lon = Double(val["lon"].string!)
            // Creates a marker in the center of the map.
            let marker = GMSMarker()
            marker.position = CLLocationCoordinate2D(latitude: lat!, longitude: lon!)
            marker.title = val["id"].string
            marker.snippet = "Australia"
            let escort_status = val["av_status"].string!
            print(escort_status)
            if escort_status == "Green" {
                marker.icon = #imageLiteral(resourceName: "green")
            } else if escort_status == "Yellow" {
                marker.icon = #imageLiteral(resourceName: "yellow")
            } else if escort_status == "Red" {
                marker.icon = #imageLiteral(resourceName: "red")
            }
            marker.map = mapView
        }
    }
    
//    func mapView(_ mapView: GMSMapView, didChange position: GMSCameraPosition) {
//        let latitude = mapView.camera.target.latitude
//        let longitude = mapView.camera.target.longitude
//        centerMapCoordinate = CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
//        self.placeMarkerOnCenter(centerMapCoordinate:centerMapCoordinate)
//    }
//    
//    func placeMarkerOnCenter(centerMapCoordinate:CLLocationCoordinate2D) {
//        let marker = GMSMarker()
//        marker.position = centerMapCoordinate
//        marker.map = self.mapView
//    }
    
    override func rightClick() {
        let vc = (storyboard?.instantiateViewController(withIdentifier: "SairVC")) as! SairVC
        vc.modalPresentationStyle = .overFullScreen
        vc.modalTransitionStyle = .crossDissolve
        vc.delegate = self
        self.present(vc, animated: true, completion: nil)
    }
    
    @IBAction func btnHome(_ sender: UIButton) {
        let objVC = self.storyboard!.instantiateViewController(withIdentifier: "SolicitarEscoltaVC") as! SolicitarEscoltaVC
        if let response = responseDict {
            objVC.responseDict = response
        }
        self.navigationController?.pushViewController(objVC, animated: true)
    }
    
    func didTappedOnLogout() {
        let objVC = self.storyboard!.instantiateViewController(withIdentifier: "LogoutVC") as! LogoutVC
        self.navigationController?.pushViewController(objVC, animated: true)
    }
    
    @IBAction func btnLocation(_ sender: UIButton) {
        
    }
}
