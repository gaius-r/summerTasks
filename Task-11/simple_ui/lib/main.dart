import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:simple_ui/constants.dart';
import 'package:simple_ui/screens/login/loginScreen.dart';
import 'package:simple_ui/screens/register/registerScreen.dart';
import 'package:simple_ui/screens/welcome/welcomeScreen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'AutoPaper',
      theme: ThemeData(
        primaryColor: kPrimaryColor,
        scaffoldBackgroundColor: Colors.white,
      ),
      initialRoute: "home",
      routes: {
        "home": (context) => WelcomeScreen(),
        "login": (context) => LoginScreen(),
        "register": (context) => RegisterScreen(),
      },
    );
  }
}
