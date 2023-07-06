import 'package:flutter/material.dart';
import 'package:universal_html/html.dart' as html;
import 'package:url_launcher/url_launcher_string.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
            child: ElevatedButton(
          child: const Text("Test Call"),
          onPressed: () async {
            // _openAPP();
            launchCaller('0333828707');
          },
        )
            // TextButton(
            //     onPressed: () {
            //       _launchURL();
            //     },
            //     child: const Text('data')),
            ),
      ),
    );
  }

  void _openAPP() {
    //  html.window.navigator.getUserMedia(audio: true, video: true);
    html.window.location.href = "tel:0333828707";
  }

  Future<void> launchCaller(String phoneNumber) async {
    String url = 'tel:$phoneNumber';
    Uri uri;
    try {
      uri = Uri.parse(url);
      await launchUrlString(uri.toString(),
          webViewConfiguration: const WebViewConfiguration(
              enableJavaScript: false, enableDomStorage: false));
      // await launchUrl(uri, mode: LaunchMode.externalApplication);
    } catch (e) {
      return;
    }
    // bool canLaunch = await canLaunchUrl(uri);
    // if (!canLaunch) {
    //   return;
    // }
    // try {
    //   await launchUrl(uri, mode: LaunchMode.platformDefault);
    // } catch (e) {
    //   return;
    // }
  }

  // Future<void> _launchURL() async {
  //   try {
  //     await launch(
  //       'tel:0333828707',
  //       customTabsOption: CustomTabsOption(
  //         toolbarColor: Colors.blue,
  //         enableDefaultShare: true,
  //         enableUrlBarHiding: true,
  //         showPageTitle: true,
  //         animation: CustomTabsSystemAnimation.slideIn(),
  //         extraCustomTabs: const <String>[
  //           // ref. https://play.google.com/store/apps/details?id=org.mozilla.firefox
  //           'org.mozilla.firefox',
  //           // ref. https://play.google.com/store/apps/details?id=com.microsoft.emmx
  //           'com.microsoft.emmx',
  //         ],
  //       ),
  //       safariVCOption: const SafariViewControllerOption(
  //         preferredBarTintColor: Colors.blue,
  //         preferredControlTintColor: Colors.white,
  //         barCollapsingEnabled: true,
  //         entersReaderIfAvailable: true,
  //         dismissButtonStyle: SafariViewControllerDismissButtonStyle.done,
  //       ),
  //     );
  //   } catch (e) {
  //     // An exception is thrown if browser app is not installed on Android device.
  //     debugPrint(e.toString());
  //   }
  // }
}
