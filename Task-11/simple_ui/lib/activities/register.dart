import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class MyRegister extends StatefulWidget {
  @override
  _MyRegisterState createState() => _MyRegisterState();
}

class _MyRegisterState extends State<MyRegister> {
  var authc = FirebaseAuth.instance;

  String email = "";
  String password = "";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Register User"),
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
              var user = await authc.createUserWithEmailAndPassword(
                  email: email, password: password);
              print(user);
            },
            child: Text("Registered"),
          ),
        ],
      ),
    );
  }
}
