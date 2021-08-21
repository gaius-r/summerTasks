import 'package:flutter/material.dart';
import 'package:simple_ui/components/account_exists_check.dart';
import 'package:simple_ui/components/rounded_button.dart';
import 'package:simple_ui/components/rounded_input_field.dart';
import 'package:simple_ui/components/rounded_password_field.dart';
import 'package:simple_ui/constants.dart';
import 'package:simple_ui/screens/authentication/firebase_auth.dart';
import 'package:simple_ui/screens/register/components/register_background.dart';

class Body extends StatelessWidget {
  const Body({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 40),
        margin: EdgeInsets.only(top: 50),
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: EdgeInsets.symmetric(vertical: 20),
                child: Text(
                  "SIGN UP",
                  textAlign: TextAlign.left,
                  style: TextStyle(
                    fontWeight: FontWeight.normal,
                    fontFamily: 'Josefin Sans',
                    fontSize: size.width * 0.1,
                    color: Colors.white,
                  ),
                ),
              ),
              RoundedInputField(
                icon: Icon(
                  Icons.person,
                  color: kPrimaryColor,
                ),
                hint: "Your Email",
                onChange: (value) {},
              ),
              RoundedPasswordField(
                onChange: (value) {},
              ),
              RoundedPasswordField(
                onChange: (value) {},
                hint: "Confirm Password",
              ),
              RoundedButton(
                press: () async {},
                text: "SIGN UP",
                color: Colors.grey.shade700,
                pressColor: Colors.black87,
                textColor: kPrimaryLightColor,
                width: size.width * 0.8,
              ),
              SizedBox(height: size.height * 0.02),
              AccountExistsCheck(
                press: () {
                  Navigator.pushReplacementNamed(context, "login");
                },
                login: false,
              )
            ],
          ),
        ),
      ),
    );
  }
}
