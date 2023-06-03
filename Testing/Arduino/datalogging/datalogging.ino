const int photodiodeCount = 8;
const int photodiodePins[photodiodeCount] = {A0, A1, A2, A3, A4, A5, A6, A7};

void setup() {
  Serial.begin(9600);
  while (!Serial) ;  // Wait for serial connection
  
  // Set photodiode pins as inputs
  for (int i = 0; i < photodiodeCount; i++) {
    pinMode(photodiodePins[i], INPUT);
  }
}

void loop() {
  // Wait for command from the computer to start data logging
  while (!Serial.available()) ;
  Serial.println("Enter 's' to start logging data, and enter 'e' to stop logging.");

  // Read the command from the computer
  char command = Serial.read();
  
  if (command == 's') {
    // Start data logging
    
    // Prompt user to enter file name
    Serial.println("Enter file name:");
    while (!Serial.available()) ;
    String fileName = Serial.readStringUntil('\n');
    
    // Prompt user to enter time
    Serial.println("Enter time:");
    while (!Serial.available()) ;
    String time = Serial.readStringUntil('\n');
    
    // Prompt user to enter y-position
    Serial.println("Enter y-position:");
    while (!Serial.available()) ;
    String yPosition = Serial.readStringUntil('\n');
    
    // Prompt user to enter angle rotations
    Serial.println("Enter angle rotations:");
    while (!Serial.available()) ;
    String angleRotations = Serial.readStringUntil('\n');
    
    // Open the Serial connection for data logging
    Serial.begin(9600);

    // Send acknowledgment to the computer
    Serial.println("start");
    
    // Open the file on the computer for writing
    Serial.print("Creating file: ");
    Serial.println(fileName);
    
    
    // Wait for a short delay
    delay(1000);
    
    // Start logging the data to the computer
    Serial.println("Data logging started...");
    
    // Open the Serial connection for data logging
    Serial.begin(9600);
    
    // Log the additional information to the file
    Serial.println("time");
    Serial.println(time);
    Serial.println("y-position");
    Serial.println(yPosition);
    Serial.println("angle rotations");
    Serial.println(angleRotations);
    
    // Log the data until receiving the stop command
    while (!Serial.available() || Serial.read() != 'e') {
      // Read and log the photodiode values
      for (int i = 0; i < photodiodeCount; i++) {
        // Read the photodiode value
        int photodiodeValue = analogRead(photodiodePins[i]);
    
        // Print the photodiode value to the Serial monitor
        Serial.print("Photodiode ");
        Serial.print(i);
        Serial.print(" Value: ");
        Serial.println(photodiodeValue);
        
      }
      
      // Delay before logging the next set of data
      delay(100);
    }
    
    // Send acknowledgment to the computer
    Serial.println("stop");
    
    // Close the Serial connection for data logging
    Serial.end();
    
    // Log the completion message
    Serial.println("Data logging complete!");
  }
}
