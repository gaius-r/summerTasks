import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:simple_ui/activities/home.dart';
import 'package:simple_ui/activities/login.dart';
import 'package:simple_ui/activities/register.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MaterialApp(
    initialRoute: "home",
    routes: {
      "home": (context) => MyHome(),
      "register": (context) => MyRegister(),
      "login": (context) => MyLogin(),
    },
  ));
}
