float ECG[] = {-0.06,-0.065,-0.06,-0.075,-0.065,-0.07,-0.07,-0.09,-0.08,-0.095,-0.08,-0.095,-0.08,-0.095,-0.085,-0.09,-0.09,-0.1,-0.085,-0.105,-0.09,-0.045,0.005,0.015,0.045,0.155,0.14,0.045,0.005,-0.04,-0.085,-0.2,-0.195,-0.2,-0.2,-0.24,-0.13,0.34,1.155,1.47,-0.155,-0.825,-0.59,-0.35,-0.155,-0.17,-0.14,-0.155,-0.115,-0.125,-0.09,-0.095,-0.065,-0.055,-0.015,-0.005,0.035,0.045,0.09,0.11,0.15,0.18,0.205,0.225,0.23,0.22,0.235,0.23,0.2,0.17,0.12,0.075,0.04,0.02,0.005,-0.005,-0.005,-0.01,-0.015,-0.01,0,-0.005,-0.02,-0.02,-0.015,-0.025,-0.035,-0.045,-0.045,-0.06,-0.065,-0.07,-0.055,-0.06,-0.08,-0.075,-0.09,-0.065,-0.075,-0.08,-0.08,-0.085,-0.09,-0.075,-0.085,-0.095,-0.105,-0.09,-0.095,-0.07,-0.045,0.005,0.03,0.07,0.195,0.145,0.05,-0.015,-0.025,-0.115,-0.18,-0.19,-0.185,-0.185,-0.215,0.01,0.575,1.185,0.96,-0.16,-0.74,-0.64,-0.35,-0.175,-0.145,-0.15,-0.145,-0.105,-0.12,-0.09,-0.085,-0.07,-0.04,-0.02,0.005,0.02,0.045,0.08,0.115,0.14,0.165,0.21,0.19,0.22,0.21,0.215,0.215,0.16,0.135,0.1,0.05,0.035,-0.005,0.005,-0.005,-0.015,-0.02,-0.01,0,-0.02,-0.005,-0.04,-0.035,-0.05,-0.04,-0.055,-0.075,-0.05,-0.075,-0.09,-0.08,-0.09,-0.08,-0.075,-0.085,-0.085,-0.095,-0.095,-0.105,-0.08,-0.115,-0.1,-0.095,-0.1,-0.075,-0.005,0.01,0.055,0.185,0.145,0.075,-0.005,-0.025,-0.11,-0.175,-0.18,-0.22,-0.175,-0.24,-0.03,0.53,1.21,1.22,-0.105,-0.795,-0.69,-0.375,-0.165,-0.155,-0.135,-0.15,-0.12,-0.12,-0.09,-0.095,-0.05,-0.05,-0.01,-0.005,0.03,0.08,0.075,0.145,0.155,0.2,0.2,0.24,0.235,0.245,0.245,0.215,0.18,0.15,0.09,0.035,0.025,0,-0.015,-0.03,0,-0.02,-0.005,-0.025,-0.03,-0.015,-0.01,-0.035,-0.04,-0.05,-0.045,-0.04,-0.075,-0.065,-0.095,-0.085,-0.085,-0.09,-0.1,-0.1,-0.08,-0.105,-0.105,-0.1,-0.105,-0.095,-0.1,-0.09,-0.035,0.01,0.035,0.07,0.19,0.125,0.045,-0.035,-0.06,-0.155,-0.21,-0.225,-0.2,-0.215,-0.265,0.07,0.865,1.495,0.625,-0.44,-0.815,-0.6,-0.31,-0.175,-0.18,-0.165,-0.135,-0.135,-0.115,-0.105,-0.085,-0.06,-0.03,-0.02,0.015,0.05,0.07,0.105,0.165,0.2,0.205,0.235,0.235,0.265,0.26,0.235,0.215,0.17,0.125,0.09,0.025,-0.015,-0.03,-0.035,-0.04,-0.04,-0.035,-0.04,-0.02,-0.04,-0.04,-0.03,-0.045,-0.065,-0.06,-0.06,-0.09,-0.08,-0.095,-0.085,-0.105,-0.09,-0.1,-0.105,-0.115,-0.1,-0.115,-0.11,-0.135,-0.095,-0.125,-0.105,-0.085,-0.015,0.02,0.03,0.135,0.16,0.105,0.03,-0.05,-0.05,-0.17,-0.205,-0.215,-0.175,-0.21,-0.215,0.175,1.09,1.7,0.335,-0.615,-0.705,-0.46,-0.175,-0.165,-0.145,-0.155,-0.115,-0.12,-0.105,-0.105,-0.085,-0.06,-0.015,-0.005,0.02,0.05,0.08,0.105,0.18,0.205,0.24,0.235,0.27,0.27,0.28,0.26,0.23,0.175,0.135,0.09,0.045,0,-0.005,-0.025,-0.025,-0.025,-0.02,0,-0.005,-0.005,-0.005,-0.005,-0.01,-0.025,-0.02,-0.04,-0.04,-0.04,-0.05,-0.06,-0.05,-0.065,-0.06,-0.07,-0.06,-0.09,-0.08,-0.095,-0.085,-0.1};
int i;
void setup() {    Serial.begin(9600);  i=0;}
void loop() {    Serial.println(ECG[i]);delay(10);  i=i+1;  if (i > sizeof(ECG)/sizeof(float)){    i=0;    }}
