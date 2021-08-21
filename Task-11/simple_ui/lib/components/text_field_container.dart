import 'package:flutter/material.dart';
import 'package:simple_ui/constants.dart';

class TextFieldContainer extends StatelessWidget {
  final Color color;
  final Widget child;
  const TextFieldContainer({
    Key? key,
    this.color = kPrimaryLightColor,
    required this.child,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Container(
      margin: EdgeInsets.symmetric(vertical: 10),
      padding: EdgeInsets.symmetric(horizontal: 10, vertical: 5),
      width: size.width * 0.8,
      decoration: BoxDecoration(
        color: color,
        borderRadius: BorderRadius.circular(30),
      ),
      child: child,
    );
  }
}
