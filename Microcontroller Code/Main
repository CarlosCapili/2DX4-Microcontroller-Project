// Carlos Capili - McMaster University
// Data acquisition program
// Bus speed is 30MHz


#include <stdint.h>
#include "tm4c1294ncpdt.h"
#include "Systick.h" 
#include "PLL.h" 
#include "2dx4_ds90-1.h"
#include "uart.h"
#include "vl53l1x_api.h"
#include "onboardLEDs.h"

void PortL5_Init(void){//Using PL5 for Displacement Status
	SYSCTL_RCGCGPIO_R |= SYSCTL_RCGCGPIO_R10;	
	while((SYSCTL_PRGPIO_R&SYSCTL_PRGPIO_R10) == 0){};   //allow time for clock to stabilize 	
	GPIO_PORTL_DIR_R |= 0xFF;             								
	GPIO_PORTL_DEN_R |= 0xFF; 
	return; 
} 

void PortM_Init(void){//used for push button
	SYSCTL_RCGCGPIO_R |= SYSCTL_RCGCGPIO_R11;            //activate the clock for Port M
	while((SYSCTL_PRGPIO_R&SYSCTL_PRGPIO_R11) == 0){};   //allow time for clock to stabilize 
	GPIO_PORTM_DIR_R |= 0b00000000;       			 				// make PM0 an input, PM0 is reading the column 
	GPIO_PORTM_DEN_R |= 0b00000001;
	return;
}


void PortN1_Init(void){//Using N1 for Distance Status
	SYSCTL_RCGCGPIO_R |= SYSCTL_RCGCGPIO_R12;                 //activate the clock for Port N 
	while((SYSCTL_PRGPIO_R&SYSCTL_PRGPIO_R12) == 0){};				//wait for clock to stabilize
	GPIO_PORTN_DIR_R|=0b00000010;                             //Using N1 for Distance Status
	GPIO_PORTN_DEN_R|=0b00000010;															//allow digital enable of output pin
	return;
}

void forward(){//forward sequence for motor - clockwise rotation
	int time = 5;//wait 10 ms

	GPIO_PORTL_DATA_R = 0b00001100; 
	SysTick_Wait10ms(time); 
	GPIO_PORTL_DATA_R = 0b00000110; 
	SysTick_Wait10ms(time); 
	GPIO_PORTL_DATA_R = 0b00000011; 
	SysTick_Wait10ms(time); 
	GPIO_PORTL_DATA_R = 0b00001001; 
	SysTick_Wait10ms(time); 
}//end of forward 
 


int main(void){
	int t=0;
	SysTick_Init(); 
	PLL_Init(); 
	PortM_Init();
	PortN1_Init(); //Distance Status LED
	PortL5_Init(); //Displacement Status LED and MOTOR
	onboardLEDs_Init();
	I2C_Init();
	UART_Init();
	Sensor_Init();
	
	int angle=0,delay=0;
	
	while(1){//keep checking if the button is pressed 
			
		GPIO_PORTL_DATA_R |= 0b00100000;//turn displacement LED on when not rotating	
		
		if((GPIO_PORTM_DATA_R&0b00000001)==0){	//Checks if push button is pressed
			
			GPIO_PORTN_DATA_R = 0b00000010;//turn on distance status LED
			GPIO_PORTL_DATA_R |= 0b00000000;//turn off displacement LED when rotating	
			
			
			while(t<512){//rotate one full revolution
			
				forward(); //drive motor to rotate clockwise direction
				t++;
				angle++;
				
				if(angle%1==0){												//captures a distance measurement every 1 degree or after each 4 step sequence
					GPIO_PORTN_DATA_R = 0b00000000;					//blink LED
					sensorRange(); //take measurement after 1 degrees
					delay++;							
				}//end of if
				if(delay<5&&delay>=1){//used to keep led off for a small amount of time to see it blink
					GPIO_PORTN_DATA_R = 0b00000000;
					delay++;
				}
				else{
					GPIO_PORTN_DATA_R = 0b00000010;//turn on distance status LED
					delay=0;
				}
					
			}//end of while
			
	
		GPIO_PORTN_DATA_R = 0b00000000;//turn off when not rotating
		t=0;//reset
			
		}
		else{
			GPIO_PORTN_DATA_R=0b00000000;
		}

	}//end of while
}//end of main
