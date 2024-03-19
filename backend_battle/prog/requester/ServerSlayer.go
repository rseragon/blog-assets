package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"sync"
	"time"
)

func main() {

  var wg sync.WaitGroup

  url := "http://flask-env.eba-zqqh36pa.ap-south-1.elasticbeanstalk.com/"
  for i := 0; i < 100000; i++ {
    wg.Add(1)
    go makeHTTPRequest(url, i, &wg)

    if i % 5000 == 0 {
      time.Sleep(time.Second * 3)
    }
  }

  wg.Wait()
}

func makeHTTPRequest(url string, i int, wg *sync.WaitGroup) {
  defer wg.Done()
  time.Sleep(time.Second)

  fmt.Printf("[GoRoutine] %d\n", i)
  resp, err := http.Get(url)

  if err != nil {
    log.Fatal(err.Error())
    return;
  }
  defer resp.Body.Close() 

  body, err := io.ReadAll(resp.Body)

  if err != nil {
    log.Print(err.Error())
    return;
  }

  fmt.Printf("[Data] %s\n", body)
}
