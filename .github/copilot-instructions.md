# Sogiza Copilot Instructions

## Project Snapshot
- Native iOS app written in Swift 4, organised under `Sogiza/Sogiza/**` with storyboards (not tracked) driving the UI.
- CocoaPods manages dependencies; open `Sogiza.xcworkspace` or run `xcodebuild -workspace Sogiza.xcworkspace -scheme Sogiza -configuration Debug` (see `.vscode/tasks.json` for the simulator build template).
- Third-party code for `MBProgressHUD` and `Reachability` lives in `Sogiza/Sogiza/Third Party Library` and is exposed via `Sogiza/Sogiza/Sogiza-Bridging-Header.h`.

## App Flow & Navigation
- `AppDelegate` (`Sogiza/Sogiza/AppDelegate.swift`) enables Google Maps, configures location updates, and delegates launch routing to `Switcher.updateRootVC()`.
- `Switcher` chooses between `LoginVC` and `HomeVC` based on `UserDefaults` key `status`; navigation is always wrapped in a `UINavigationController`.
- Logout uses the modal `SairVC` (`ViewControllers/Pop Ups/SairVC.swift`) to confirm before `LogoutVC.swift` clears all `UserDefaults` keys and re-calls `Switcher`.

## Networking & Data
- REST endpoints and API keys are hard-coded in `Common/Constant.swift`; the backend lives at `http://technorizen.com/sogiza/webservice/`.
- `CommunicationManeger` (`Utility/CommunicationManager.swift`) wraps Alamofire `POST` calls and image uploads, gated by `Utility.checkNetworkConnectivityWithDisplayAlert` (Reachability).
- JSON responses are parsed with SwiftyJSON inside the view controllers (see `LoginVC` for auth and `HomeVC`/`SolicitarEscoltaVC` for guard lookups and escort requests).

## Location & Maps
- `LocationManager` singleton (`Utility/LocationManager.swift`) centralises CoreLocation permissions and delegates; controllers adopt `LocationManagerDelegate` for updates.
- `HomeVC` renders guards on a `GMSMapView`, colouring markers with `#imageLiteral` assets (`Assets.xcassets`) and pushes `SolicitarEscoltaVC` with the fetched guard array.
- `SolicitarEscoltaVC` also requests location to include the user's coordinates when calling `END_POINT_ACCEPT_REQUEST`.

## UI Patterns & Utilities
- Navigation bar helpers, alerts, and `MBProgressHUD` progress indicators are provided by `Extension/ViewControllerExt.swift`.
- Input validation lives in `Utility/Utility.swift`; login masking relies on `InputMask` delegates wired via IBOutlet references in `LoginVC`.
- `CustomCells/SolicitarEscoltaCell.swift` uses a delegate protocol (`requestProtocol`) to bubble table-row button taps back to `SolicitarEscoltaVC`.

## Working With Pods
- Pods are checked into source control (`Sogiza/Pods/**`); keep versions aligned with `Podfile` (note the smart quotes around some version constraints).
- When adding a new dependency, update `Podfile`, run `pod install`, and commit both the updated `Podfile.lock` and the generated pods to keep the workspace consistent.

## Gotchas
- Many strings are Portuguese; preserve existing copy unless product specifies otherwise.
- `CommunicationManeger` is misspelled across the codebase (follow the existing type name to avoid breaking references).
- Google Maps requies `GOOGLE_API_KEY` in `Common/Constant.swift`; check env/security policy before rotating the key.
