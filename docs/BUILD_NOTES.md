# iOS (Sogiza)

- Copie `ios/Sogiza/Sogiza/Common/Secrets.sample.plist` para `Secrets.plist` e informe:
  - `GOOGLE_MAPS_API_KEY`
  - `API_BASE_URL` (com `/` ao final)
- `cd ios/Sogiza && pod install` sempre que atualizar dependências.
- Abra `Sogiza.xcworkspace` e selecione o esquema **Sogiza**. O app inicializa `Switcher.updateRootVC()` em `AppDelegate.swift`.
- Dependências principais via CocoaPods: Google Maps, IQKeyboardManagerSwift, SwiftyJSON, Alamofire.
- Build e testes podem ser comandados pelo VS Code `tasks.json` ou diretamente pelo Xcode.

# Android

## Estrutura
- Escolta: `android/escort/SOGIZAESCORT` (AGP 7.4.2, AndroidX).
- Morador: `android/morador/SOGIZA` (AGP 7.4.2, AndroidX).

## Preparação
1. Em cada projeto crie/edite `local.properties` com:
   ```properties
   sdk.dir=/caminho/para/Android/Sdk
   GOOGLE_MAPS_API_KEY=chave_android
   API_BASE_URL=https://exemplo.com/sogiza/webservice/
   ```
2. O script Gradle injeta `google_maps_key` (Manifest) e `BuildConfig.API_BASE_URL` (Retrofit).
3. Compile com `./gradlew clean assembleDebug`. O wrapper usa Gradle 7.5.1 + Java 11.
4. Dependências atualizadas: AndroidX, Retrofit 2.9, Firebase/Play Services via BOM, Glide 4.15, Picasso 2.8.

# Checklist de validação
- Inserir credenciais válidas e confirmar login, listagem de guardas e fluxo “Solicitar Escolta” em ambos os apps.
- Validar localização/GPS, notificações push (Firebase Messaging) e atualização de markers no mapa.
- Conferir que `API_BASE_URL` aponta para backend funcional (HTTP 200) e que o certificado HTTPS é aceito.
- Garantir que as chaves Google Maps (iOS/Android) estão habilitadas para os pacotes `com.tech.sogizaescort` e `com.techno.sogiza`.
- Em builds de produção configurar perfis de assinatura (iOS) e `signingConfigs` no Gradle (Android) antes de gerar binaries finais.
