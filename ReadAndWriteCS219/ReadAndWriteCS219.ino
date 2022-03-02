/**
 * ----------------------------------------------------------------------------
 * This is a MFRC522 library example; see https://github.com/miguelbalboa/rfid
 * for further details and other examples.
 *
 * NOTE: The library file MFRC522.h has a lot of useful info. Please read it.
 *
 * Released into the public domain.
 * ----------------------------------------------------------------------------
 * This sample shows how to read and write data blocks on a MIFARE Classic PICC
 * (= card/tag).
 *
 * BEWARE: Data will be written to the PICC, in sector #1 (blocks #4 to #7).
 *
 *
 * Typical pin layout used:
 * -----------------------------------------------------------------------------------------
 *             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
 *             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
 * Signal      Pin          Pin           Pin       Pin        Pin              Pin
 * -----------------------------------------------------------------------------------------
 * RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
 * SPI SS      SDA(SS)      10            53        D10        10               10
 * SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
 * SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
 * SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
 *
 * More pin layouts for other boards can be found here: https://github.com/miguelbalboa/rfid#pin-layout
 *
 */

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9           // Configurable, see typical pin layout above
#define SS_PIN          10          // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

MFRC522::MIFARE_Key key;

int testFlag;
/**
 * Initialize.
 */
void setup() {
    Serial.begin(9600); // Initialize serial communications with the PC
    while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
    SPI.begin();        // Init SPI bus
    mfrc522.PCD_Init(); // Init MFRC522 card

    // Prepare the key (used both as key A and as key B)
    // using FFFFFFFFFFFFh which is the default at chip delivery from the factory
    for (byte i = 0; i < 6; i++) {
        key.keyByte[i] = 0xFF;
    }
    testFlag = 0;
/*
    Serial.println(F("Scan a MIFARE Classic PICC to demonstrate read and write."));
    Serial.print(F("Using key (for A and B):"));
    dump_byte_array(key.keyByte, MFRC522::MF_KEY_SIZE);
    Serial.println();

    Serial.println(F("BEWARE: Data will be written to the PICC, in sector #1"));*/
}

/**
 * Main loop.
 */
void loop() {
    byte songBuffer[22];
    /*while (Serial.available() == 0) {
      
    }
    while (Serial.available() > 0) {
          //String data = Serial.readStringUntil('\n');
          Serial.readBytes(songBuffer, 1);
          //data.getBytes(songBuffer, 22);
    }
    for (int i = 0; i < 16; i++) {
      Serial.println(songBuffer[i]);
    }*/
    if (testFlag == 0) {
      /*while(1) {
        if (Serial.available() > 0) {
            String data = Serial.readStringUntil('\n');
            byte buffer[22];
            data.getBytes(buffer, 22);
            for (int i = 0; i < 22; i++) {
              Serial.println(buffer[i]);
            }
        }
      }*/
      // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
      if ( ! mfrc522.PICC_IsNewCardPresent())
          return;
  
      // Select one of the cards
      if ( ! mfrc522.PICC_ReadCardSerial())
          return;
      
      // Show some details of the PICC (that is: the tag/card)
      //Serial.print(F("Card UID:"));
      dump_byte_array(mfrc522.uid.uidByte, mfrc522.uid.size);
      //Serial.println();
      //Serial.print(F("PICC type: "));
      MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
      //Serial.println(mfrc522.PICC_GetTypeName(piccType));
  
      // Check for compatibility
      /*if (    piccType != MFRC522::PICC_TYPE_MIFARE_MINI
          &&  piccType != MFRC522::PICC_TYPE_MIFARE_1K
          &&  piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
          Serial.println(F("This sample only works with MIFARE Classic cards."));
          return;
      }*/
  
      // In this sample we use the second sector,
      // that is: sector #1, covering block #4 up to and including block #7
      byte sector         = 1;
      byte trailerBlock   = 7;
      MFRC522::StatusCode status;
      byte buffer[18];
      byte size = sizeof(buffer);

      String x = "14gmLQPNYokqB80KxAp69f";
      x.getBytes(songBuffer, 22);
      
      for (int i = 0; i < 22; i++) {
        Serial.println(songBuffer[i]);
      }
      Serial.println("--");
      // Authenticate using key A
      //Serial.println(F("Authenticating using key A..."));
      status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, trailerBlock, &key, &(mfrc522.uid));
      if (status != MFRC522::STATUS_OK) {
          Serial.print(F("PCD_Authenticate() failed: "));
          Serial.println(mfrc522.GetStatusCodeName(status));
          return;
      }
  
      
      // Write data to the block
      //Serial.print(F("Writing data into block ")); Serial.print(blockAddr);
      //Serial.println(F(" ..."));
      //dump_byte_array(dataBlock, 16); Serial.println();
      byte dataBlock1[16];
      byte dataBlock2[16];
      
      for (int i = 0; i < 16; i++) {
          dataBlock1[i] = songBuffer[i];
      }
      
      for (int i = 0; i < 16; i++) {
          if (i < 6) {
            dataBlock2[i] = songBuffer[i+16];
          } else {
            dataBlock2[i] = 0;
          }
      }
      byte blockAddr = 4;
      status = (MFRC522::StatusCode) mfrc522.MIFARE_Write(blockAddr, dataBlock1, 16);
      if (status != MFRC522::STATUS_OK) {
          Serial.print(F("MIFARE_Write() failed: "));
          Serial.println(mfrc522.GetStatusCodeName(status));
      }
      blockAddr = 5;
      status = (MFRC522::StatusCode) mfrc522.MIFARE_Write(blockAddr, dataBlock2, 16);
      if (status != MFRC522::STATUS_OK) {
          Serial.print(F("MIFARE_Write() failed: "));
          Serial.println(mfrc522.GetStatusCodeName(status));
      }
  
      /*byte blockAddr = 7;
      byte dataBlock[16];
      for (int i = 0; i < 16; i++) {
          if (i == 9) {
            dataBlock[i] = songBuffer[21];
            Serial.println(dataBlock[i]);
            Serial.println(songBuffer[21]);
            Serial.println("-------");
          } else{
            dataBlock[i] = 0x00;
          }
      }
      status = (MFRC522::StatusCode) mfrc522.MIFARE_Write(blockAddr, dataBlock, 16);
      if (status != MFRC522::STATUS_OK) {
          Serial.print(F("MIFARE_Write() failed: "));
          Serial.println(mfrc522.GetStatusCodeName(status));
      }*/
      //Serial.println();
  
      
      // Read data from the block (again, should now be what we have written)
      /*
      Serial.print(F("Reading data from block ")); Serial.print(blockAddr);
      Serial.println(F(" ..."));*/
      for (int block = 4; block < 6; block++) {
        byte blockAddr = block;
        status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(blockAddr, buffer, &size);
        /*if (status != MFRC522::STATUS_OK) {
            Serial.print(F("MIFARE_Read() failed: "));
            Serial.println(mfrc522.GetStatusCodeName(status));
        }*/
        //Serial.print(F("Data in block ")); Serial.print(blockAddr); Serial.println(F(":"));
        //dump_byte_array(buffer, 16); Serial.println();
        byte* data = buffer;
        for (int i = 0; i < 16; i++) {
          Serial.println(data[i]);
        }
        Serial.println("-----");
      }
      
      // Halt PICC
      mfrc522.PICC_HaltA();
      // Stop encryption on PCD
      mfrc522.PCD_StopCrypto1();
      testFlag = 1;
      
    }
}

/**
 * Helper routine to dump a byte array as hex values to Serial.
 */
void dump_byte_array(byte *buffer, byte bufferSize) {
    for (byte i = 0; i < bufferSize; i++) {
        Serial.print(buffer[i] < 0x10 ? " 0" : " ");
        Serial.print(buffer[i], HEX);
    }
}
