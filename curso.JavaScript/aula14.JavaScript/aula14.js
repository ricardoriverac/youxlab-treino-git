mbti = 'istj'

switch(mbti){
    case "istj": case "estj": case "isfj": case "esfj":
        console.log("Você é " + mbti)
        console.log("Você é Sentinela")
        console.log("----------------------")
        console.log('SENTINELAS: istj, estj, isfj, esfj')
        break
    case "estp": case "istp": case "isfp": case "esfp":
        console.log("Você é " + mbti)
        console.log("Você é Explorador")
        console.log("----------------------")
        console.log('EXPLORADORES: estp, istp, esfp, isfp')
        break
    case "infp": case "enfp": case "enfj": case "infj":
        console.log("Você é " + mbti)
        console.log("Você é Diplomata")
        console.log("----------------------")
        console.log('DIPLOMATAS: enfp, infp, enfj, infp')
        break
    default:
        console.log("Você é " + mbti)
        console.log("Você é um Analista")
        console.log("----------------------")
        console.log('ANALISTAS: entp, intp, entj, intj')
        break
    
    
    
}