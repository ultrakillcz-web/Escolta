//
//  Environment.swift
//  Sogiza
//
//  Created by Codex on 18/10/25.
//

import Foundation

struct Environment {
    let googleMapsAPIKey: String
    let baseURL: String

    static let current: Environment = {
        guard let url = Bundle.main.url(forResource: "Secrets", withExtension: "plist") else {
            fatalError("Secrets.plist is missing. Copy Secrets.sample.plist and provide valid values.")
        }

        guard let data = try? Data(contentsOf: url),
              let dictionary = try? PropertyListSerialization.propertyList(from: data, options: [], format: nil) as? [String: Any] else {
            fatalError("Secrets.plist could not be parsed. Ensure it contains valid plist data.")
        }

        guard let googleKey = dictionary["GOOGLE_MAPS_API_KEY"] as? String, !googleKey.isEmpty else {
            fatalError("GOOGLE_MAPS_API_KEY missing in Secrets.plist")
        }

        guard let base = dictionary["API_BASE_URL"] as? String, !base.isEmpty else {
            fatalError("API_BASE_URL missing in Secrets.plist")
        }
        return Environment(googleMapsAPIKey: googleKey, baseURL: base)
    }()
}

