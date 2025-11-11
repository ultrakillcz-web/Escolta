//
//  AppDelegate.swift
//  Sogiza
//
//  Created by mac on 18/10/18.
//  Copyright © 2018 Technorizen. All rights reserved.
//

import UIKit
import IQKeyboardManagerSwift
import GoogleMaps
import CoreLocation
import UserNotifications

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, CLLocationManagerDelegate, UNUserNotificationCenterDelegate {

    var window: UIWindow?
    var locationManager = CLLocationManager()
    var currentLocation: CLLocation?
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        IQKeyboardManager.shared.enable = true
        Switcher.updateRootVC()
        GMSServices.provideAPIKey(GOOGLE_API_KEY)
     
        self.locationManager.delegate = self
        self.locationManager.requestWhenInUseAuthorization()
        self.locationManager.desiredAccuracy = kCLLocationAccuracyBest
        self.locationManager.startUpdatingLocation()
        configureNotifications(for: application)
        return true
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
       currentLocation = locations.last
    }

    func applicationWillResignActive(_ application: UIApplication) {
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
    }

    func applicationWillTerminate(_ application: UIApplication) {
    }
    
    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
        print("APNS device token: \(token)")
    }
    
    func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {
        print("Failed to register for remote notifications: \(error.localizedDescription)")
    }
    
    func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
        if let appResponse = userInfo["aps"] as? [String: Any],
           let alertMsg = appResponse["alert"] as? String,
           let presenter = UIApplication.topViewController() {
            DispatchQueue.main.async {
                let alertController = UIAlertController(title: "Notification", message: alertMsg, preferredStyle: .alert)
                alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
                presenter.present(alertController, animated: true, completion: nil)
            }
        }
        completionHandler(.noData)
    }
    
    private func configureNotifications(for application: UIApplication) {
        let center = UNUserNotificationCenter.current()
        center.delegate = self
        center.requestAuthorization(options: [.alert, .badge, .sound]) { granted, error in
            if let error = error {
                print("Notification authorization error: \(error.localizedDescription)")
            }
            guard granted else { return }
            DispatchQueue.main.async {
                application.registerForRemoteNotifications()
            }
        }
    }
}

