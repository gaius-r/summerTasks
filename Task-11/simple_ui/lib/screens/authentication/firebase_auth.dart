import 'package:firebase_auth/firebase_auth.dart';

Future<bool> signIn(String email, String password) async {
  try {
    var user = await FirebaseAuth.instance
        .signInWithEmailAndPassword(email: email, password: password);
    print(user);
    return true;
  } on FirebaseAuthException catch (e) {
    if (e.code == 'invalid-email') {
      print('The given email is invalid.');
    } else if (e.code == 'user-not-found') {
      print("No account was found with the given email. Please Sign Up");
    } else if (e.code == 'wrong-password') {
      print("Incorrect Password.");
    }
    return false;
  } catch (e) {
    print(e.toString());
    return false;
  }
}

Future<bool> signUp(String email, String password) async {
  try {
    var user = await FirebaseAuth.instance
        .createUserWithEmailAndPassword(email: email, password: password);
    print(user);
    return true;
  } on FirebaseAuthException catch (e) {
    if (e.code == 'weak-password') {
      print('The pass provided is too weak.');
    } else if (e.code == 'email-already-in-use') {
      print("The account already exists for that email.");
    }
    return false;
  } catch (e) {
    print(e.toString());
    return false;
  }
}
