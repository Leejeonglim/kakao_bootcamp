const API_BASE = ""; // 같은 도메인/포트 기준 (예: http://localhost:8000)

async function fetchPosts() {
  try {
    const res = await fetch(`${API_BASE}/posts/`);
    if (!res.ok) throw new Error("목록 조회 실패");
    const posts = await res.json();

    const list = document.getElementById("postList");
    list.innerHTML = "";

    posts.forEach((p) => {
      const li = document.createElement("li");
      li.className = "post-item";
      li.innerHTML = `
        <div class="post-header">
          <span class="post-title">[${p.id}] ${escapeHtml(p.title)}</span>
          <span class="post-author">${escapeHtml(p.author)}</span>
        </div>
        <p class="post-content">${escapeHtml(p.content)}</p>
        <div class="post-footer">
          <small>${p.created_at}</small>
          <button data-id="${p.id}" class="delete-btn">삭제</button>
        </div>
      `;
      list.appendChild(li);
    });

    document.querySelectorAll(".delete-btn").forEach((btn) => {
      btn.addEventListener("click", async (e) => {
        const id = e.target.getAttribute("data-id");
        await deletePost(id);
      });
    });
  } catch (err) {
    alert("게시글 목록을 불러오는 중 오류가 발생했습니다.");
    console.error(err);
  }
}

async function createPost(data) {
  try {
    const res = await fetch(`${API_BASE}/posts/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    const json = await res.json().catch(() => ({}));

    if (!res.ok) {
      throw new Error(json.detail || "작성 실패");
    }

    await fetchPosts();
  } catch (err) {
    alert(`게시글 작성 중 오류: ${err.message}`);
    console.error(err);
  }
}

async function deletePost(id) {
  try {
    const res = await fetch(`${API_BASE}/posts/${id}`, {
      method: "DELETE",
    });
    if (!res.ok) {
      const json = await res.json().catch(() => ({}));
      throw new Error(json.detail || "삭제 실패");
    }
    await fetchPosts();
  } catch (err) {
    alert(`삭제 중 오류: ${err.message}`);
    console.error(err);
  }
}

function escapeHtml(str) {
  if (!str) return "";
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("postForm");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = {
      title: document.getElementById("title").value.trim(),
      author: document.getElementById("author").value.trim(),
      content: document.getElementById("content").value.trim(),
    };
    if (!data.title || !data.author || !data.content) {
      alert("모든 필드를 입력해주세요.");
      return;
    }
    await createPost(data);
    form.reset();
  });

  fetchPosts();
});
