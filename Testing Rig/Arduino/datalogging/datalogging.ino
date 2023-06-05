#define NUMBER_OF_MUX 3
#define NUMBER_OF_CHANNELS 8

// Assign the Arduino pins connected to the multiplexer
int sPins[NUMBER_OF_MUX][3] = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
int zPin[NUMBER_OF_MUX] = {A0, A1, A2};

void setup() {
  Serial.begin(9600);
  while (!Serial) ;  // Wait for serial connection

  // Set the select pins as outputs
  for (int i = 0; i < NUMBER_OF_MUX; i++) {
    for (int j = 0; j < 3; j++) {
      pinMode(sPins[i][j], OUTPUT);
    }
    pinMode(zPin[i], INPUT);
  }
}

void loop() {
  // Wait for command from the computer to start data logging
  while (!Serial.available()) ;
  Serial.println("start");

  // Read the command from the computer
  char command = Serial.read();
  
  if (command == 's') {
    // Start data logging
    
    // Send acknowledgment to the computer
    Serial.println("start");
    
    // Log the data until receiving the stop command
    while (!Serial.available() || Serial.read() != 'e') {
      // Read and send the photodiode values
      for (int i = 0; i < NUMBER_OF_MUX; i++) {
        for (int j = 0; j < NUMBER_OF_CHANNELS; j++) {
          // Set the select pins for the current channel
          for (int k = 0; k < 3; k++) {
            digitalWrite(sPins[i][k], bitRead(j, k));
          }

          // Read the photodiode value
          int photodiodeValue = analogRead(zPin[i]);
      
          // Send the photodiode value to the computer
          Serial.print("Photodiode ");
          Serial.print((i * NUMBER_OF_CHANNELS) + j);
          Serial.print(" Value: ");
          Serial.println(photodiodeValue);
        }
      }
      
      // Delay before sending the next set of data
      delay(100);
    }
    
    // Send acknowledgment to the computer
    Serial.println("stop");
    
    // Wait for the computer to acknowledge the stop command
    while (!Serial.available()) ;
    while (Serial.read() != 'stop') ;
    
    // Log the completion message to the computer
    Serial.println("Data logging complete!");
 
