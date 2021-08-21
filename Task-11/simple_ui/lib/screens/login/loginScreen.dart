import 'package:flutter/material.dart';
import 'package:simple_ui/constants.dart';
import 'package:simple_ui/screens/login/components/login_body.dart';

class LoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: kPrimaryColor,
      body: Body(),
    );
  }
}
