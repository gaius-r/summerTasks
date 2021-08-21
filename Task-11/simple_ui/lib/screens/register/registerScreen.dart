import 'package:flutter/material.dart';
import 'package:simple_ui/constants.dart';
import 'package:simple_ui/screens/register/components/register_body.dart';

class RegisterScreen extends StatelessWidget {
  const RegisterScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: kPrimaryColor,
      body: Body(),
    );
  }
}
