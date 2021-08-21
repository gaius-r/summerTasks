import 'package:flutter/material.dart';
import 'package:simple_ui/components/rounded_button.dart';
import 'package:simple_ui/constants.dart';
import 'package:simple_ui/screens/components/background.dart';

class Body extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // provides height and width of the screen
    Size size = MediaQuery.of(context).size;
    return Background(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          SizedBox(height: size.height * 0.03),
          Padding(
            padding: EdgeInsets.symmetric(vertical: 20),
            child: Text(
              "AutoPaper",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 30,
                fontFamily: 'Josefin Sans',
              ),
            ),
          ),
          RoundedButton(
              text: "LOGIN",
              width: size.width * 0.8,
              press: () {
                Navigator.pushNamed(context, "login");
              }),
          RoundedButton(
            text: "SIGN UP",
            width: size.width * 0.8,
            color: kPrimaryLightColor,
            textColor: kPrimaryColor,
            pressColor: kPrimaryColor,
            press: () {
              Navigator.pushNamed(context, "register");
            },
          ),
        ],
      ),
    );
  }
}
