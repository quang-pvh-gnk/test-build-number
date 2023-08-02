// Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// ignore_for_file: public_member_api_docs

import 'dart:async';

import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'URL Launcher',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'URL Launcher'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool _hasCallSupport = false;
  Future<void>? _launched;
  final String _phone = '';

  @override
  void initState() {
    super.initState();
    // Check for phone call support.
    canLaunchUrl(Uri(scheme: 'tel', path: '0333828707')).then((bool result) {
      setState(() {
        _hasCallSupport = result;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.title),
        ),
        body: Column(
          children: [
            TextButton(
              child: const Text('phone'),
              onPressed: () {
                launchCaller('0333828707');
              },
            ),
            TextButton(
              child: const Text('link'),
              onPressed: () {
                launchNewPage(
                    'https://ssl.fdoc.jp/reserve/subjectlist/index/cid/s0381154?SITE_CODE=hp&_ga=2.66457326.1744645754.1655947314-72516926.1643593405');
              },
            ),
          ],
        ));
  }

  Future<void> launchCaller(String phoneNumber) async {
    String url = 'tel:$phoneNumber';
    Uri uri;
    try {
      uri = Uri.parse(url);
    } catch (e) {
      return;
    }
    bool canLaunch = await canLaunchUrl(uri);
    if (!canLaunch) {
      return;
    }
    try {
      await launchUrl(uri);
    } catch (e) {
      return;
    }
  }

  Future<void> launchNewPage(String url) async {
    Uri uri;
    try {
      uri = Uri.parse(url);
    } catch (e) {
      return;
    }
    bool canLaunch = await canLaunchUrl(uri);
    if (!canLaunch) {
      return;
    }
    try {
      await launchUrl(
        uri,
        webOnlyWindowName: '_blank',
      );
    } catch (e) {
      return;
    }
  }
}
