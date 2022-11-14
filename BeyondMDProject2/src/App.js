import React, { useState } from 'react';
import { Document, Page } from 'react-pdf/dist/esm/entry.webpack5';
import { AppBar, Toolbar, Button, Box, Typography, Stack, Divider } from '@mui/material';

function App() {
  const [buttonColorHello, setButtonColorHello] = useState("primary");
  const [buttonColorResume, setButtonColorResume] = useState("primary");
  const [buttonColorApiData, setButtonColorApiData] = useState("primary");
  const [displayItem, setDisplayItem] = useState("");

  // When the "DISPLAY HELLO" button is clicked it'll call this displayHello() function
  function displayHello(){
    if (buttonColorHello === "primary") {
      setButtonColorHello("success");
      setButtonColorResume("primary");
      setButtonColorApiData("primary");

      // By clicking the button it'll change the state of displayItem to the following below
      setDisplayItem(
        <div>
          <Typography variant="h4">Hello BeyondMD!</Typography>
        </div>
      );
    } else {
      // If the button is already clicked, it will simply reset the color and display
      setButtonColorHello("primary");
      setButtonColorResume("primary");
      setButtonColorApiData("primary");
      setDisplayItem("");
    }
  }

  // When the "DISPLAY RESUME" button is clicked it'll call this displayResume() function
  function displayResume() {
    if (buttonColorResume === "primary") {
      setButtonColorHello("primary");
      setButtonColorResume("success");
      setButtonColorApiData("primary");
      
      // By clicking the button it'll change the state of displayItem to the following below
      setDisplayItem(
        /*
        React-pdf is very useful for displaying PDFs. All you really need are two components
        which are Document and Page. The default location of the PDF must be in public folder.
        Since my PDF only contained 1 page, the pageNumber can be set to 1.
        
        However, if it has multiple pages it's possible to have state in pageNumber. When a
        button is clicked it will either increase or decrease the page number. In return, it
        will also change the PDF page number.
        */
        <div>
          <Document file="resume_template.pdf">
            <Page pageNumber={1} renderTextLayer={false} renderAnnotationLayer={false}/>
          </Document>
        </div>
      );
    } else {
      // If the button is already clicked, it will simply reset the button color and reset displayItem
      setButtonColorHello("primary");
      setButtonColorResume("primary");
      setButtonColorApiData("primary");
      setDisplayItem("");
    }
  }

  // await keyword can only be used in a async function
  // When the "DISPLAY API DATA" button is clicked it'll call this displayApiData() async function
  async function displayApiData() {
    if (buttonColorApiData === "primary") {
      setButtonColorHello("primary");
      setButtonColorResume("primary");
      setButtonColorApiData("success");

      // Fetch returns a promise which needs to wait until the value is fulfilled
      const data = await fetch('https://api.openweathermap.org/data/2.5/forecast?q=Atlanta,US&APPID=' + process.env.REACT_APP_OPENWEATHERMAP_API + "&units=imperial");
      const apiData = await data.json();
      const dayOneWeather = {
        date_time: apiData.list[8].dt_txt + " UTC",
        temp_f: apiData.list[8].main["temp"],
        icon: "http://openweathermap.org/img/wn/" + apiData.list[8].weather[0]["icon"] + "@2x.png",
        description: apiData.list[8].weather[0]["description"]
      }
      const dayTwoWeather = {
        date_time: apiData.list[16].dt_txt + " UTC",
        temp_f: apiData.list[16].main["temp"],
        icon: "http://openweathermap.org/img/wn/" + apiData.list[16].weather[0]["icon"] + "@2x.png",
        description: apiData.list[16].weather[0]["description"]
      }
      const dayThreeWeather = {
        date_time: apiData.list[24].dt_txt + " UTC",
        temp_f: apiData.list[24].main["temp"],
        icon: "http://openweathermap.org/img/wn/" + apiData.list[24].weather[0]["icon"] + "@2x.png",
        description: apiData.list[24].weather[0]["description"]
      }
      const dayFourWeather = {
        date_time: apiData.list[32].dt_txt + " UTC",
        temp_f: apiData.list[32].main["temp"],
        icon: "http://openweathermap.org/img/wn/" + apiData.list[32].weather[0]["icon"] + "@2x.png",
        description: apiData.list[32].weather[0]["description"]
      }
      
      // If the button is already clicked, it will simply reset the button color and reset displayItem
      setDisplayItem(
        <div>
          <br></br>
          <Typography variant="h4"><u>Atlanta's Weather Forecast</u></Typography>
          <br></br>
          <hr></hr>
          <Stack direction="row" justifyContent="center" divider={<Divider orientation="vertical" flexItem/>} spacing={2}>
            <div>
              <Typography variant="h5">{dayOneWeather.date_time}</Typography>
              <hr></hr>
              <Typography variant="h5">{dayOneWeather.temp_f}°F</Typography>
              <img src={dayOneWeather.icon} width="200" height="200" alt="Weather Icon"></img>
              <Typography variant="h5">{dayOneWeather.description}</Typography>
            </div>
            <div>
              <Typography variant="h5">{dayTwoWeather.date_time}</Typography>
              <hr></hr>
              <Typography variant="h5">{dayTwoWeather.temp_f}°F</Typography>
              <img src={dayTwoWeather.icon} width="200" height="200" alt="Weather Icon"></img>
              <Typography variant="h5">{dayTwoWeather.description}</Typography>
            </div>
            <div>
              <Typography variant="h5">{dayThreeWeather.date_time}</Typography>
              <hr></hr>
              <Typography variant="h5">{dayThreeWeather.temp_f}°F</Typography>
              <img src={dayThreeWeather.icon} width="200" height="200" alt="Weather Icon"></img>
              <Typography variant="h5">{dayThreeWeather.description}</Typography>
            </div>
            <div>
              <Typography variant="h5">{dayFourWeather.date_time}</Typography>
              <hr></hr>
              <Typography variant="h5">{dayFourWeather.temp_f}°F</Typography>
              <img src={dayFourWeather.icon} width="200" height="200" alt="Weather Icon"></img>
              <Typography variant="h5">{dayFourWeather.description}</Typography>
            </div>
          </Stack>
          <hr></hr>
        </div>
      );
    } else {
      // If the button is already clicked, it will simply reset the button color and reset displayItem
      setButtonColorHello("primary");
      setButtonColorResume("primary");
      setButtonColorApiData("primary");
      setDisplayItem("");
    }
  }

  return (
    <div>
      <AppBar position="static" color="secondary">
        <Toolbar>
          <Button sx={{ margin: 'auto' }} variant="contained" color={buttonColorHello} onClick={() => { displayHello(); }}>Display Hello</Button>
          <Button sx={{ margin: 'auto' }} variant="contained" color={buttonColorResume} onClick={() => { displayResume(); }}>Display Resume</Button>
          <Button sx={{ margin: 'auto' }} variant="contained" color={buttonColorApiData} onClick={() => { displayApiData(); }}>Display API Data</Button>
        </Toolbar>
      </AppBar>
      <br></br>
      <Box align='center'>
        {displayItem}
      </Box>
    </div>
  );
}

export default App;
