import 'package:flutter/material.dart';
import 'package:simple_ui/components/text_field_container.dart';
import 'package:simple_ui/constants.dart';

class RoundedInputField extends StatelessWidget {
  final Icon icon;
  final String hint;
  final Color color;
  final ValueChanged<String> onChange;
  const RoundedInputField({
    Key? key,
    this.hint = "",
    this.color = kPrimaryLightColor,
    required this.onChange,
    required this.icon,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextFieldContainer(
      child: TextField(
        onChanged: onChange,
        decoration: InputDecoration(
          icon: icon,
          hintText: hint,
          border: InputBorder.none,
        ),
        style: TextStyle(
          fontSize: 18,
        ),
      ),
      color: color,
    );
  }
}
