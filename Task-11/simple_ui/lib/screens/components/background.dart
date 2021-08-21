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
      height: size.height,
      width: double.infinity,
      child: Stack(
        alignment: Alignment.center,
        children: [
          Positioned(
            top: -size.width * 0.2,
            left: -size.width * 0.3,
            child: Image.asset("assets/images/abst_circle_top_left.png"),
            width: size.width * 0.95,
          ),
          Positioned(
            bottom: -size.width * 0.1,
            right: -size.width * 0.2,
            child: Image.asset("assets/images/abst_circle_bottom_right.png"),
            width: size.width * 0.8,
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 30),
            child: child,
          ),
          child,
        ],
      ),
    );
  }
}
