import { useLocation } from "react-router-dom";
import { useState, useEffect } from "react";

import Message from "../layout/Message";
import Container from "../layout/Container";
import LinkButton from "../layout/LinkButton";

import styles from "./Projects.module.css";
import ProjectCard from "../project/ProjectCard";

function Projects() {
  const [projects, setProjects] = useState([]);

  const location = useLocation();
  let message = "";
  if (location.state) {
    message = location.state.message;
  }

  useEffect(() => {
    fetch("http://localhost:5001/projects", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((resp) => resp.json())
      .then((data) => {
          setProjects(data);
        })
        .catch((err) => console.log(err));
    }, []);
    
    return (
        <div className={styles.project_container}>
      <div className={styles.title_container}>
        <h1>Meus Projetos</h1>
        <LinkButton to="/newproject" text="Criar Projeto" />
      </div>
        {/* {console.log("projects ",projects.map((e)=>e.category?.name || "Sem categoria"))} */}
      {message && <Message type="success" msg={message} />}
      <Container customClass="start">
        {projects.length > 0 &&
            projects.map((project)=>(
                <ProjectCard 
                    id={project.id}
                    name={project.name}
                    budget={project.budget}
                    category={project.category?.name || "Sem categoria"}
                    key={project.id}
                />
            ))
        }
    </Container>
    </div>
  );
}

export default Projects;
