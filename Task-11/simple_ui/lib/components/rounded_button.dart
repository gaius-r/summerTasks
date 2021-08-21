import 'package:flutter/material.dart';
import 'package:simple_ui/constants.dart';

class RoundedButton extends StatelessWidget {
  final String text;
  final VoidCallback press;
  final Color color, pressColor, textColor;
  final double width;
  const RoundedButton({
    Key? key,
    required this.text,
    required this.press,
    required this.width,
    this.color = kPrimaryColor,
    this.pressColor = Colors.white,
    this.textColor = Colors.white,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(vertical: 10),
      width: width,
      child: ClipRRect(
        borderRadius: BorderRadius.circular(30),
        child: TextButton(
          onPressed: press,
          child: Text(
            text,
            style: TextStyle(
              color: textColor,
              fontSize: 18,
              fontWeight: FontWeight.bold,
              fontFamily: 'Josefin Sans',
            ),
          ),
          style: TextButton.styleFrom(
            padding: EdgeInsets.symmetric(vertical: 20, horizontal: 40),
            primary: pressColor,
            backgroundColor: color,
          ),
        ),
      ),
    );
  }
}
