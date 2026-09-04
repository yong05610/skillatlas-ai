@'
document.getElementById("testBtn").addEventListener("click", async () => {
  const result = document.getElementById("result");

  try {
    const response = await fetch("/api/hello");
    const data = await response.text();
    result.textContent = data;
  } catch (error) {
    result.textContent = "API 호출 실패";
    console.error(error);
  }
});
'@ | Set-Content js\app.js