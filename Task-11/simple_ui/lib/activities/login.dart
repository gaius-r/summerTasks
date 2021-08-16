import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class MyLogin extends StatefulWidget {
  @override
  _MyLoginState createState() => _MyLoginState();
}

class _MyLoginState extends State<MyLogin> {
  var authc = FirebaseAuth.instance;
  String email = "", password = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Login"),
      ),
      body: Column(
        children: [
          TextField(
            onChanged: (value) {
              email = value;
            },
          ),
          TextField(
            onChanged: (value) {
              password = value;
            },
          ),
          ElevatedButton(
            onPressed: () async {
              print("Email : " + email);
              print("Password : " + password);
              try {
                var user = await authc.signInWithEmailAndPassword(
                    email: email, password: password);
              } on FirebaseAuthException catch (e) {
                print("User does not exist");
              }
            },
            child: Text("Logged In"),
          ),
        ],
      ),
    );
  }
}
