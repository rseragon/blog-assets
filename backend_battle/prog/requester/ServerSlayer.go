package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"sync"
	"time"
)

func main() {

  if len(os.Args) < 2 {
    fmt.Printf("Usage: %s URL\n", os.Args[0])
    os.Exit(0)
  }

  var wg sync.WaitGroup

  url := os.Args[1]
  for i := 0; i < 100000; i++ {
    wg.Add(1)
    go makeHTTPRequest(url, i, &wg)

    if i % 1000 == 0 {
      time.Sleep(time.Second * 1)
    }
  }

  wg.Wait()
  fmt.Println("Finished!")
}

func makeHTTPRequest(url string, i int, wg *sync.WaitGroup) {
  defer wg.Done()
  time.Sleep(time.Second)

  fmt.Printf("[GoRoutine(%d)] {%s}\n", i, time.Now().Format(time.RFC850))
  resp, err := http.Get(url)

  if err != nil {
    log.Fatal("[Error]", err.Error())
    return;
  }
  defer resp.Body.Close() 

  body, err := io.ReadAll(resp.Body)

  if err != nil {
    log.Print("[Error]", err.Error())
    return;
  }

  fmt.Printf("[Data(%d)] %s {%s}\n", i, body, time.Now().Format(time.RFC850))
}
