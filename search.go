package main

import (
	//"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
)

// Making it easy to document
type Entry struct {
	BSSID	string
	Latitude string
	Longitude string
}


func main() {

	// Open the file
	csvfile, _ := os.Open("short.csv")

	// Parse the file
	r := csv.NewReader(csvfile)

	var entries []String
	
	// Iterate through the records
	for {
		// Read each record from csv
		record, err := r.Read()
		if err == io.EOF {
			break
		}

		// Create a struct to hold values
		data := Entry {
			BSSID: record.[0],
			Latitude: record.[1],
			Longitude: record.[2],
		}
		


	}
}
