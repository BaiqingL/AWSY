package main

import (
	"github.com/prologic/bitcask"
	"encoding/csv"
	"fmt"
	"io"
	"os"
	"sync"
	//"reflect"
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

	 arguments:= make([]string, len(os.Args))

	if len(os.Args) > 1 {
		for _, BSSIDs := range os.Args[1:] {
		arguments = append(arguments, BSSIDs)
		}
	}

	// Initialize the waitgroup
	var waitgroup sync.WaitGroup

	for _, ids := range arguments {
		waitgroup.Add(1)
		go func(val interface{}) {
	
			fmt.Println(search(ids, db, &waitgroup))
			
		}(ids)
	}
	waitgroup.Wait()



	// Finished reading, start searching
	/*
	var result string
	done := make(chan bool)
	go func() {
		result = search("003A983DEC71", db)
		done <- true
	}()
	<-done

	fmt.Println(result)
	*/

}

func search(BSSID string, db *bitcask.Bitcask, waitgroup *sync.WaitGroup) string {
	val, _ := db.Get([]byte(BSSID))
	waitgroup.Done()
	return BSSID + " " + string(val)
}
