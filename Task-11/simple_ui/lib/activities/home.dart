import 'package:flutter/material.dart';

class MyHome extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Home"),
      ),
      body: Column(
        children: [
          ElevatedButton(
            onPressed: () {
              print("Going to register");
              Navigator.pushNamed(context, "register");
            },
            child: Text("Register"),
          ),
          ElevatedButton(
            onPressed: () {
              print("Going to login");
              Navigator.pushNamed(context, "login");
            },
            child: Text("Login"),
          ),
        ],
      ),
    );
  }
}
