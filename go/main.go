package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

const language = "Go"

func indexHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.NotFound(w, r)
		return
	}

	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "<h1>Hello World for %s</h1>", language)
}

func languageHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	response := map[string]string{
		"language": language,
	}

	json.NewEncoder(w).Encode(response)
}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/language", languageHandler)

	log.Println("Go server is running on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}
