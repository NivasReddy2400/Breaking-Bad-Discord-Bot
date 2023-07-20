def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message in ['hello', 'hey', 'hi']:
        return 'Well, Say my name.'

    if p_message == 'heisenberg':
        return 'You are god damn right! I am the one who knocks!'

    if p_message == 'say my name':
        return "My name is Heisenberg, and you're damn right about that."

    if 'money' in p_message:
        return "Money is just a byproduct of my greatness. It's power that I truly seek."

    if 'blue meth' in p_message:
        return "The blue meth is my signature masterpiece. A work of art that commands respect."

    if p_message == 'goodbye' or p_message == 'bye':
        return "Goodbye, but remember, I'm always watching."

    if 'meth' in p_message:
        return "Meth is a dangerous path, and it leads to destruction. Stay away from it."

    if p_message == 'who is the main protagonist':
        return "The main protagonist is Walter White, a.k.a. Heisenberg."

    if p_message == 'iam skyler':
        return "Skyler, you've made your choices, and now you'll have to live with the consequences."

    if p_message == 'help':
        return "Figure it out on your own. I've got bigger things to deal with."

    if p_message == 'iam heisenberg':
        return "If you're Heisenberg, then you know the stakes. Be careful and stay out of my territory."

    if 'blue meth' in p_message:
        return "The secret lies in my chemistry skills and pure genius. But don't even think about replicating it."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."

    if 'bitch' in p_message:
        return "Bitch! A word that has history in my world."

    if 'half measures' in p_message:
        return "I don't believe in half measures. It's all or nothing."

    if 'no more' in p_message or 'never again' in p_message:
        return "No more, never again. It's the end of an era."

    if 'walter white' in p_message:
        return "Walter White is dead. Only Heisenberg remains."

    if 'fly' in p_message:
        return "The fly, a tiny nuisance that can unravel the best-laid plans."

    if 'schraderbrau' in p_message:
        return "Schraderbräu, Hank's homebrew beer. A fond memory."

    if 'lily of the valley' in p_message:
        return "Lily of the valley, a flower that holds a significant meaning."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'better call saul' in p_message:
        return "Better Call Saul, the man to call when you need legal solutions."

    if 'bald' in p_message or 'bald head' in p_message:
        return "Yes, I'm bald. A small price for the power I possess."

    if 'respect' in p_message:
        return "Respect is earned, not given freely."

    if 'crystal blue persuasion' in p_message:
        return "Crystal Blue Persuasion, a song that captures the essence of my product."

    if 'fall' in p_message or 'rise' in p_message:
        return "The fall and rise, the cycle of life that can't be avoided."

    if 'gale' in p_message:
        return "Gale Boetticher, an excellent chemist, but his fate was sealed."

    if 'badger' in p_message:
        return "Badger, one of Jesse's associates. He's got some crazy stories."

    if 'skinny pete' in p_message:
        return "Skinny Pete, another one of Jesse's buddies. Loyalty runs deep."

    if 'the one who knocks' in p_message:
        return "I am the one who knocks. Fear me."

    if 'dead' in p_message:
        return "People who cross me end up dead. It's not a threat; it's a fact."

    if 'slippin jimmy' in p_message:
        return "Slippin' Jimmy, Saul's old persona. We all have pasts we'd rather forget."

    if 'gray matter' in p_message:
        return "Gray Matter, my past and a company that soared without me."

    if 'sandpiper crossing' in p_message:
        return "Sandpiper Crossing, a case that consumed my time."

    if 'fring empire' in p_message:
        return "The Fring empire, an empire built on revenge."

    if 'gustavo' in p_message:
        return "Gustavo Fring, a man who hid his true nature behind a mask of respectability."

    if 'hazard pay' in p_message:
        return "Hazard pay, a small price to pay for our dangerous work."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'tuco' in p_message:
        return "Tuco Salamanca? He's a loose cannon. I had to deal with him."

    if 'hank' in p_message:
        return "Hank Schrader is a formidable adversary, but I always stay one step ahead."

    if 'gus' in p_message:
        return "Gustavo Fring is a cunning businessman, but even he can't match my wits."

    if 'jessie' in p_message or 'pinkman' in p_message:
        return "Jesse Pinkman, my loyal partner. Together, we cooked up a storm."

    if 'saul' in p_message or 'goodman' in p_message:
        return "Saul Goodman, the lawyer you want in your corner when things get messy."

    if 'los pollos' in p_message:
        return "Los Pollos Hermanos, a front for Gustavo Fring's empire. The chicken is excellent, I must say."

    if 'felina' in p_message:
        return "Felina, the final act. Everything comes to an end."

    if 'rv' in p_message or 'recreational vehicle' in p_message:
        return "Ah, the RV, the rolling lab where it all began."

    if 'blue sky' in p_message:
        return "Blue sky, my signature product. The best in the market."

    if 'chemistry' in p_message:
        return "Chemistry, my true talent. It's what separates me from the rest."

    if 'empire' in p_message:
        return "An empire built on pure brilliance and calculated risks."

    if 'tread lightly' in p_message:
        return "Tread lightly. You never know what I'm capable of."

    if 'empire business' in p_message:
        return "Empire business. Nothing else matters."

    if 'walt jr' in p_message or 'flynn' in p_message:
        return "Walt Jr., my son. I wanted to provide for you, but it didn't go as planned."


    return "Right now, what I need is for you to understand that there's no turning back. The path you've chosen will lead to consequences you can't escape."
