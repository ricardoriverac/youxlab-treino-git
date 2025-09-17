import styles from './MyButton.module.css' //foi importado o css do botão

function MyButton() {
  return <button className={styles.button}>I'm a button</button>;  
  // className={style.NomeDaClasseDoCss}
}

export default MyButton
