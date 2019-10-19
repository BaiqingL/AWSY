package main

import (
	"github.com/prologic/bitcask"
	"encoding/csv"
	"fmt"
	"io"
	"os"
	"sync"
)

func main() {

	// Opens up temporary database
    db, _ := bitcask.Open("/tmp/db")
	defer db.Close()

	// Open the file
	csvfile, _ := os.Open("short.csv")

	// Parse the file
	r := csv.NewReader(csvfile)
	
	// Iterate through the records
	for {
		// Read each record from csv
		record, err := r.Read()
		if err == io.EOF {
			break
		}

		db.Put([]byte(record[0]),[]byte(record[1]+","+record[2]))
		
	}

	// Take arguments, 0 element is the actual command
	var arguments []string
	if len(os.Args) > 1 {
		arguments = os.Args[1:]
	} else {
		fmt.Println("No BSSID given")
		return
	}

	fmt.Printf("%v\n", arguments)

	// Initialize the waitgroup
	var waitgroup sync.WaitGroup

	for _, ids := range arguments {
		waitgroup.Add(1)
		//fmt.Println(ids)
		go func(val string) {
			fmt.Println(search(val, db, &waitgroup))
			
		}(ids)
	}
	waitgroup.Wait()

}

func search(BSSID string, db *bitcask.Bitcask, waitgroup *sync.WaitGroup) string {
	val, _ := db.Get([]byte(BSSID))
	waitgroup.Done()
	return BSSID + " " + string(val)
}
