import 'package:flutter/material.dart';

class Background extends StatelessWidget {
  final Widget child;
  const Background({
    Key? key,
    required this.child,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Container(
      width: double.infinity,
      height: size.height,
      child: Stack(
        alignment: Alignment.center,
        children: [
          Positioned(
            top: -size.width * 0.4,
            right: -size.width * 0.4,
            child: Image.asset(
              "assets/images/abst_circle_white_top_right.png",
              width: size.width * 0.9,
            ),
          ),
          Positioned(
            bottom: -size.width * 0.2,
            left: -size.width * 0.2,
            child: Image.asset(
              "assets/images/abst_circle_white_bottom_left.png",
              width: size.width * 0.6,
            ),
          ),
          child,
        ],
      ),
    );
  }
}
