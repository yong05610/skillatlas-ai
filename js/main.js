const form = document.getElementById("roadmapForm");
const formMessage = document.getElementById("formMessage");
const loadingMessage = document.getElementById("loadingMessage");
const roadmapResult = document.getElementById("roadmapResult");
const submitButton = document.getElementById("submitButton");

const REQUIRED_FIELDS = ["level", "goal", "duration", "studyTime"];
const GENERIC_ERROR = "로드맵 생성 중 문제가 발생했습니다. 잠시 후 다시 시도해주세요.";

function getFormData() {
  const data = new FormData(form);

  return {
    level: String(data.get("level") || "").trim(),
    goal: String(data.get("goal") || "").trim(),
    duration: String(data.get("duration") || "").trim(),
    studyTime: String(data.get("studyTime") || "").trim(),
    interests: String(data.get("interests") || "").trim(),
    extra: String(data.get("extra") || "").trim(),
  };
}

function hasMissingRequired(payload) {
  return REQUIRED_FIELDS.some((field) => !payload[field]);
}

function hasTooLongInput(payload) {
  return payload.interests.length > 200 || payload.extra.length > 500;
}

function setLoading(isLoading) {
  submitButton.disabled = isLoading;
  submitButton.textContent = isLoading ? "생성 중..." : "로드맵 생성하기";
  loadingMessage.hidden = !isLoading;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const payload = getFormData();
  formMessage.textContent = "";

  if (hasMissingRequired(payload)) {
    formMessage.textContent = "필수 항목을 입력한 후 다시 시도해주세요.";
    return;
  }

  if (hasTooLongInput(payload)) {
    formMessage.textContent = "입력 내용이 너무 깁니다. 내용을 줄인 후 다시 시도해주세요.";
    return;
  }

  setLoading(true);
  roadmapResult.textContent = "요청을 처리하고 있습니다.";

  try {
    const response = await fetch("/api/generate-roadmap", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok || !data.result) {
      throw new Error("Roadmap request failed");
    }

    roadmapResult.textContent = data.result;
  } catch (error) {
    roadmapResult.textContent = GENERIC_ERROR;
  } finally {
    setLoading(false);
  }
});
