/*
Package main is a simple program that checks the availability of web services
by sending HTTP GET requests. 

It uses an HTTP client with a defined timeout to perform the checks
and prints the results based on the HTTP status code.
*/
package request

import (
	"fmt"
	"net/http"
	"time"
)

/*
checkHTTP sends an HTTP GET request to the specified URL and prints the result.

Parameters:
  - url: The URL to test.

Returns:
  - None. The results are printed directly to the console.
*/
func checkHTTP(url string) {
	// Define a 5-second timeout for the request
	client := http.Client{Timeout: 5 * time.Second}

	// Send the HTTP GET request
	resp, err := client.Get(url)

	// Check if the request failed
	if err != nil {
		fmt.Printf("[ERROR] Can't connect to %s : %v\n", url, err)
		return
	}

	// Check the HTTP status code
	if resp.StatusCode == 200 {
		fmt.Printf("[OK] Service available: %s\n", url)
	} else {
		fmt.Printf("[ERROR] Service unavailable (%d): %s\n", resp.StatusCode, url)
	}
}

/*
The main function initializes a list of URLs to test
and calls the checkHTTP function for each URL in the list.
*/
func main() {
	// List of URLs to test
	urls := []string{
		"https://example.com/",
		"https://google.com/",
	}

	// Test each URL
	for _, url := range urls {
		checkHTTP(url)
	}
}
