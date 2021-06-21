## Task-6 : Facial Recognition with Haar cascade

So this task operates in the following manner,

- Collect sample images of the user
- Train the model with the sample set
- Run the video capture device again, and if face is recognized,
	- Send an Email to a recipient
	- Send a WhatsApp message to a recipient
	- Create an EC2 instance
	- Create an EBS volume of size 5GB
	- Attach the volume to the instance

### Pre-requisites

To keep this code short (as short as I could make it atleast), I've performed many actions before-hand which you might not have.
This code runs based on the following assumptions:

- You have opencv-python, opencv-contrib-python (and of course the other libraries that are imported) installed for python.
- You have a directory '/faces/user' relative to the program's location in your system. You can also choose to change the directory by changing the ``path`` variable under the Face Extractor section.
  Another option would be to simply add code to create a directory through the program itself using the os module.
- You have a video capture device (pretty obvious I guess). 
- You have a gmail account with the option "Allow less secure apps" enabled (this will be the sender mail).
- For the WhatsApp message to work, your default browser must already be logged in to your WhatsApp account.
- Coming to AWS, you have your IAM user credentials set either by making a file ``~/.aws/credentials`` or by using AWS CLI. Refer [this](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
- The keypair you're using (``keyPair = 'testkey'``), already exists with the same name in your AWS console. 
  You can also choose to create a key-pair through the program by uncommenting the ``create_key_pair()`` function.