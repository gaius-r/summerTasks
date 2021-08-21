import 'package:flutter/material.dart';
import 'package:simple_ui/components/text_field_container.dart';
import 'package:simple_ui/constants.dart';

class RoundedPasswordField extends StatelessWidget {
  final Color color;
  final String hint;
  final ValueChanged<String> onChange;
  const RoundedPasswordField({
    Key? key,
    this.color = kPrimaryColor,
    required this.onChange,
    this.hint = "Your Password",
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextFieldContainer(
      child: TextField(
        obscureText: true,
        onChanged: onChange,
        decoration: InputDecoration(
          hintText: hint,
          icon: Icon(
            Icons.lock,
            color: color,
          ),
          suffixIcon: Icon(
            Icons.visibility,
            color: color,
          ),
          border: InputBorder.none,
        ),
        style: TextStyle(
          fontSize: 18,
        ),
      ),
    );
  }
}
