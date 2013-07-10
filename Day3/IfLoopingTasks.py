# -*- coding: utf-8 -*-
"""

Please note each number is an individual task, you should run your code after each
task

1. To test if out run the following comparisons below:
    (please type these out instead of copying them)
print 1>3
print 3<4
print 2==2
A=4
print 3==A
print 4==A
print A<=2
print A<=4
print A<=8

run your code after this. Make sure the answers are what you'd expect

2. Combinging if elseif, else, and for.
    if you are still having problems with for loops, please do the for loop
    tutorial, othterwise move forward with this.
Loop through range(100)
for any number divisible by 3 print 'fizz'
for any number divisible by 5 print 'buzz'
for any number divisible by both print 'fizzbuzz'
for all other numbers print the number
(remember the modulo commmand % gets you the remainder so 3%3=0 as does 6%3=0
Also consider using if, elseif, and else

you can either over write your old code or just write this below it,
run it once done.

3. While looping.
Below all of this you will find the whole first scene of Hamlet split into a list by
individual word. (To declare this variable you could just remove the three " above and below it)
Suppose you wanted to capture the first 100 words with the letter e in them
use a while loop (iterting a number that moves you through hamlet and checking
the size of your variable wih the while loop)
combined with an if loop to write the list variable 
Ewords until you get 100 words.

Hints: don't forget the in command such as 'e' in word
Hint: don't forget the len() command

4. I have made two groups of animals below, and given them scores.
AnimalVar=['Injury','Injury','Injury','Injury','Control','Control','Control','Injury','Control','Control','Control','Injury','Control','Injury','Control']
 Scores=[1,2,2,1,4,4,5,3,1,4,3,1,2,3,4]
 Get the mean by groups (eg by injury or control)
 Use for/if/else to accompplish this task.
 Consider making two lists
 InjuryVar=[]
 ControlVar=[]
 and taking the mean outside the loops.
Consider taking the ttest of the two groups.
mean can be found in 
import numpy as np
np.mean(Var)
ttest can be found in
import scipy.stats
scipy.stats.ttest_ind(Var1,Var2)

"""
































""""
IWasntKidding=['ACT', 'I\n\nSCENE', 'I.', 'Elsinore.', 'A', 'platform', 'before', 'the', 'castle.\n\nFRANCISCO', 'at', 'his', 'post.', 'Enter', 'to', 'him', "BERNARDO\nBERNARDO\nWho's", 'there?\nFRANCISCO\nNay,', 'answer', 'me:', 'stand,', 'and', 'unfold', 'yourself.\nBERNARDO\nLong', 'live', 'the', 'king!\nFRANCISCO\nBernardo?\nBERNARDO\nHe.\nFRANCISCO\nYou', 'come', 'most', 'carefully', 'upon', 'your', "hour.\nBERNARDO\n'Tis", 'now', 'struck', 'twelve;', 'get', 'thee', 'to', 'bed,', 'Francisco.\nFRANCISCO\nFor', 'this', 'relief', 'much', 'thanks:', "'tis", 'bitter', 'cold,\nAnd', 'I', 'am', 'sick', 'at', 'heart.\nBERNARDO\nHave', 'you', 'had', 'quiet', 'guard?\nFRANCISCO\nNot', 'a', 'mouse', 'stirring.\nBERNARDO\nWell,', 'good', 'night.\nIf', 'you', 'do', 'meet', 'Horatio', 'and', 'Marcellus,\nThe', 'rivals', 'of', 'my', 'watch,', 'bid', 'them', 'make', 'haste.\nFRANCISCO\nI', 'think', 'I', 'hear', 'them.', 'Stand,', 'ho!', "Who's", 'there?\nEnter', 'HORATIO', 'and', 'MARCELLUS\n\nHORATIO\nFriends', 'to', 'this', 'ground.\nMARCELLUS\nAnd', 'liegemen', 'to', 'the', 'Dane.\nFRANCISCO\nGive', 'you', 'good', 'night.\nMARCELLUS\nO,', 'farewell,', 'honest', 'soldier:\nWho', 'hath', 'relieved', 'you?\nFRANCISCO\nBernardo', 'has', 'my', 'place.\nGive', 'you', 'good', 'night.\nExit\n\nMARCELLUS\nHolla!', 'Bernardo!\nBERNARDO\nSay,\nWhat,', 'is', 'Horatio', 'there?\nHORATIO\nA', 'piece', 'of', 'him.\nBERNARDO\nWelcome,', 'Horatio:', 'welcome,', 'good', 'Marcellus.\nMARCELLUS\nWhat,', 'has', 'this', 'thing', "appear'd", 'again', 'to-night?\nBERNARDO\nI', 'have', 'seen', 'nothing.\nMARCELLUS\nHoratio', 'says', "'tis", 'but', 'our', 'fantasy,\nAnd', 'will', 'not', 'let', 'belief', 'take', 'hold', 'of', 'him\nTouching', 'this', 'dreaded', 'sight,', 'twice', 'seen', 'of', 'us:\nTherefore', 'I', 'have', 'entreated', 'him', 'along\nWith', 'us', 'to', 'watch', 'the', 'minutes', 'of', 'this', 'night;\nThat', 'if', 'again', 'this', 'apparition', 'come,\nHe', 'may', 'approve', 'our', 'eyes', 'and', 'speak', 'to', 'it.\nHORATIO\nTush,', 'tush,', "'twill", 'not', 'appear.\nBERNARDO\nSit', 'down', 'awhile;\nAnd', 'let', 'us', 'once', 'again', 'assail', 'your', 'ears,\nThat', 'are', 'so', 'fortified', 'against', 'our', 'story\nWhat', 'we', 'have', 'two', 'nights', 'seen.\nHORATIO\nWell,', 'sit', 'we', 'down,\nAnd', 'let', 'us', 'hear', 'Bernardo', 'speak', 'of', 'this.\nBERNARDO\nLast', 'night', 'of', 'all,\nWhen', 'yond', 'same', 'star', "that's", 'westward', 'from', 'the', 'pole\nHad', 'made', 'his', 'course', 'to', 'illume', 'that', 'part', 'of', 'heaven\nWhere', 'now', 'it', 'burns,', 'Marcellus', 'and', 'myself,\nThe', 'bell', 'then', 'beating', 'one,--\nEnter', 'Ghost\n\nMARCELLUS\nPeace,', 'break', 'thee', 'off;', 'look,', 'where', 'it', 'comes', 'again!\nBERNARDO\nIn', 'the', 'same', 'figure,', 'like', 'the', 'king', "that's", 'dead.\nMARCELLUS\nThou', 'art', 'a', 'scholar;', 'speak', 'to', 'it,', 'Horatio.\nBERNARDO\nLooks', 'it', 'not', 'like', 'the', 'king?', 'mark', 'it,', 'Horatio.\nHORATIO\nMost', 'like:', 'it', 'harrows', 'me', 'with', 'fear', 'and', 'wonder.\nBERNARDO\nIt', 'would', 'be', 'spoke', 'to.\nMARCELLUS\nQuestion', 'it,', 'Horatio.\nHORATIO\nWhat', 'art', 'thou', 'that', "usurp'st", 'this', 'time', 'of', 'night,\nTogether', 'with', 'that', 'fair', 'and', 'warlike', 'form\nIn', 'which', 'the', 'majesty', 'of', 'buried', 'Denmark\nDid', 'sometimes', 'march?', 'by', 'heaven', 'I', 'charge', 'thee,', 'speak!\nMARCELLUS\nIt', 'is', 'offended.\nBERNARDO\nSee,', 'it', 'stalks', 'away!\nHORATIO\nStay!', 'speak,', 'speak!', 'I', 'charge', 'thee,', 'speak!\nExit', "Ghost\n\nMARCELLUS\n'Tis", 'gone,', 'and', 'will', 'not', 'answer.\nBERNARDO\nHow', 'now,', 'Horatio!', 'you', 'tremble', 'and', 'look', 'pale:\nIs', 'not', 'this', 'something', 'more', 'than', 'fantasy?\nWhat', 'think', 'you', "on't?\nHORATIO\nBefore", 'my', 'God,', 'I', 'might', 'not', 'this', 'believe\nWithout', 'the', 'sensible', 'and', 'true', 'avouch\nOf', 'mine', 'own', 'eyes.\nMARCELLUS\nIs', 'it', 'not', 'like', 'the', 'king?\nHORATIO\nAs', 'thou', 'art', 'to', 'thyself:\nSuch', 'was', 'the', 'very', 'armour', 'he', 'had', 'on\nWhen', 'he', 'the', 'ambitious', 'Norway', 'combated;\nSo', "frown'd", 'he', 'once,', 'when,', 'in', 'an', 'angry', 'parle,\nHe', 'smote', 'the', 'sledded', 'Polacks', 'on', 'the', "ice.\n'Tis", 'strange.\nMARCELLUS\nThus', 'twice', 'before,', 'and', 'jump', 'at', 'this', 'dead', 'hour,\nWith', 'martial', 'stalk', 'hath', 'he', 'gone', 'by', 'our', 'watch.\nHORATIO\nIn', 'what', 'particular', 'thought', 'to', 'work', 'I', 'know', 'not;\nBut', 'in', 'the', 'gross', 'and', 'scope', 'of', 'my', 'opinion,\nThis', 'bodes', 'some', 'strange', 'eruption', 'to', 'our', 'state.\nMARCELLUS\nGood', 'now,', 'sit', 'down,', 'and', 'tell', 'me,', 'he', 'that', 'knows,\nWhy', 'this', 'same', 'strict', 'and', 'most', 'observant', 'watch\nSo', 'nightly', 'toils', 'the', 'subject', 'of', 'the', 'land,\nAnd', 'why', 'such', 'daily', 'cast', 'of', 'brazen', 'cannon,\nAnd', 'foreign', 'mart', 'for', 'implements', 'of', 'war;\nWhy', 'such', 'impress', 'of', 'shipwrights,', 'whose', 'sore', 'task\nDoes', 'not', 'divide', 'the', 'Sunday', 'from', 'the', 'week;\nWhat', 'might', 'be', 'toward,', 'that', 'this', 'sweaty', 'haste\nDoth', 'make', 'the', 'night', 'joint-labourer', 'with', 'the', 'day:\nWho', "is't", 'that', 'can', 'inform', 'me?\nHORATIO\nThat', 'can', 'I;\nAt', 'least,', 'the', 'whisper', 'goes', 'so.', 'Our', 'last', 'king,\nWhose', 'image', 'even', 'but', 'now', "appear'd", 'to', 'us,\nWas,', 'as', 'you', 'know,', 'by', 'Fortinbras', 'of', 'Norway,\nThereto', "prick'd", 'on', 'by', 'a', 'most', 'emulate', 'pride,\nDared', 'to', 'the', 'combat;', 'in', 'which', 'our', 'valiant', 'Hamlet--\nFor', 'so', 'this', 'side', 'of', 'our', 'known', 'world', "esteem'd", 'him--\nDid', 'slay', 'this', 'Fortinbras;', 'who', 'by', 'a', "seal'd", 'compact,\nWell', 'ratified', 'by', 'law', 'and', 'heraldry,\nDid', 'forfeit,', 'with', 'his', 'life,', 'all', 'those', 'his', 'lands\nWhich', 'he', 'stood', 'seized', 'of,', 'to', 'the', 'conqueror:\nAgainst', 'the', 'which,', 'a', 'moiety', 'competent\nWas', 'gaged', 'by', 'our', 'king;', 'which', 'had', "return'd\nTo", 'the', 'inheritance', 'of', 'Fortinbras,\nHad', 'he', 'been', 'vanquisher;', 'as,', 'by', 'the', 'same', 'covenant,\nAnd', 'carriage', 'of', 'the', 'article', "design'd,\nHis", 'fell', 'to', 'Hamlet.', 'Now,', 'sir,', 'young', 'Fortinbras,\nOf', 'unimproved', 'mettle', 'hot', 'and', 'full,\nHath', 'in', 'the', 'skirts', 'of', 'Norway', 'here', 'and', "there\nShark'd", 'up', 'a', 'list', 'of', 'lawless', 'resolutes,\nFor', 'food', 'and', 'diet,', 'to', 'some', 'enterprise\nThat', 'hath', 'a', 'stomach', "in't;", 'which', 'is', 'no', 'other--\nAs', 'it', 'doth', 'well', 'appear', 'unto', 'our', 'state--\nBut', 'to', 'recover', 'of', 'us,', 'by', 'strong', 'hand\nAnd', 'terms', 'compulsatory,', 'those', 'foresaid', 'lands\nSo', 'by', 'his', 'father', 'lost:', 'and', 'this,', 'I', 'take', 'it,\nIs', 'the', 'main', 'motive', 'of', 'our', 'preparations,\nThe', 'source', 'of', 'this', 'our', 'watch', 'and', 'the', 'chief', 'head\nOf', 'this', 'post-haste', 'and', 'romage', 'in', 'the', 'land.\nBERNARDO\nI', 'think', 'it', 'be', 'no', 'other', 'but', "e'en", 'so:\nWell', 'may', 'it', 'sort', 'that', 'this', 'portentous', 'figure\nComes', 'armed', 'through', 'our', 'watch;', 'so', 'like', 'the', 'king\nThat', 'was', 'and', 'is', 'the', 'question', 'of', 'these', 'wars.\nHORATIO\nA', 'mote', 'it', 'is', 'to', 'trouble', 'the', "mind's", 'eye.\nIn', 'the', 'most', 'high', 'and', 'palmy', 'state', 'of', 'Rome,\nA', 'little', 'ere', 'the', 'mightiest', 'Julius', 'fell,\nThe', 'graves', 'stood', 'tenantless', 'and', 'the', 'sheeted', 'dead\nDid', 'squeak', 'and', 'gibber', 'in', 'the', 'Roman', 'streets:\nAs', 'stars', 'with', 'trains', 'of', 'fire', 'and', 'dews', 'of', 'blood,\nDisasters', 'in', 'the', 'sun;', 'and', 'the', 'moist', 'star\nUpon', 'whose', 'influence', "Neptune's", 'empire', 'stands\nWas', 'sick', 'almost', 'to', 'doomsday', 'with', 'eclipse:\nAnd', 'even', 'the', 'like', 'precurse', 'of', 'fierce', 'events,\nAs', 'harbingers', 'preceding', 'still', 'the', 'fates\nAnd', 'prologue', 'to', 'the', 'omen', 'coming', 'on,\nHave', 'heaven', 'and', 'earth', 'together', 'demonstrated\nUnto', 'our', 'climatures', 'and', 'countrymen.--\nBut', 'soft,', 'behold!', 'lo,', 'where', 'it', 'comes', 'again!\nRe-enter', "Ghost\n\nI'll", 'cross', 'it,', 'though', 'it', 'blast', 'me.', 'Stay,', 'illusion!\nIf', 'thou', 'hast', 'any', 'sound,', 'or', 'use', 'of', 'voice,\nSpeak', 'to', 'me:\nIf', 'there', 'be', 'any', 'good', 'thing', 'to', 'be', 'done,\nThat', 'may', 'to', 'thee', 'do', 'ease', 'and', 'grace', 'to', 'me,\nSpeak', 'to', 'me:\nCock', 'crows\n\nIf', 'thou', 'art', 'privy', 'to', 'thy', "country's", 'fate,\nWhich,', 'happily,', 'foreknowing', 'may', 'avoid,', 'O,', 'speak!\nOr', 'if', 'thou', 'hast', 'uphoarded', 'in', 'thy', 'life\nExtorted', 'treasure', 'in', 'the', 'womb', 'of', 'earth,\nFor', 'which,', 'they', 'say,', 'you', 'spirits', 'oft', 'walk', 'in', 'death,\nSpeak', 'of', 'it:', 'stay,', 'and', 'speak!', 'Stop', 'it,', 'Marcellus.\nMARCELLUS\nShall', 'I', 'strike', 'at', 'it', 'with', 'my', 'partisan?\nHORATIO\nDo,', 'if', 'it', 'will', 'not', "stand.\nBERNARDO\n'Tis", "here!\nHORATIO\n'Tis", "here!\nMARCELLUS\n'Tis", 'gone!\nExit', 'Ghost\n\nWe', 'do', 'it', 'wrong,', 'being', 'so', 'majestical,\nTo', 'offer', 'it', 'the', 'show', 'of', 'violence;\nFor', 'it', 'is,', 'as', 'the', 'air,', 'invulnerable,\nAnd', 'our', 'vain', 'blows', 'malicious', 'mockery.\nBERNARDO\nIt', 'was', 'about', 'to', 'speak,', 'when', 'the', 'cock', 'crew.\nHORATIO\nAnd', 'then', 'it', 'started', 'like', 'a', 'guilty', 'thing\nUpon', 'a', 'fearful', 'summons.', 'I', 'have', 'heard,\nThe', 'cock,', 'that', 'is', 'the', 'trumpet', 'to', 'the', 'morn,\nDoth', 'with', 'his', 'lofty', 'and', 'shrill-sounding', 'throat\nAwake', 'the', 'god', 'of', 'day;', 'and,', 'at', 'his', 'warning,\nWhether', 'in', 'sea', 'or', 'fire,', 'in', 'earth', 'or', 'air,\nThe', 'extravagant', 'and', 'erring', 'spirit', 'hies\nTo', 'his', 'confine:', 'and', 'of', 'the', 'truth', 'herein\nThis', 'present', 'object', 'made', 'probation.\nMARCELLUS\nIt', 'faded', 'on', 'the', 'crowing', 'of', 'the', 'cock.\nSome', 'say', 'that', 'ever', "'gainst", 'that', 'season', 'comes\nWherein', 'our', "Saviour's", 'birth', 'is', 'celebrated,\nThe', 'bird', 'of', 'dawning', 'singeth', 'all', 'night', 'long:\nAnd', 'then,', 'they', 'say,', 'no', 'spirit', 'dares', 'stir', 'abroad;\nThe', 'nights', 'are', 'wholesome;', 'then', 'no', 'planets', 'strike,\nNo', 'fairy', 'takes,', 'nor', 'witch', 'hath', 'power', 'to', 'charm,\nSo', "hallow'd", 'and', 'so', 'gracious', 'is', 'the', 'time.\nHORATIO\nSo', 'have', 'I', 'heard', 'and', 'do', 'in', 'part', 'believe', 'it.\nBut,', 'look,', 'the', 'morn,', 'in', 'russet', 'mantle', 'clad,\nWalks', "o'er", 'the', 'dew', 'of', 'yon', 'high', 'eastward', 'hill:\nBreak', 'we', 'our', 'watch', 'up;', 'and', 'by', 'my', 'advice,\nLet', 'us', 'impart', 'what', 'we', 'have', 'seen', 'to-night\nUnto', 'young', 'Hamlet;', 'for,', 'upon', 'my', 'life,\nThis', 'spirit,', 'dumb', 'to', 'us,', 'will', 'speak', 'to', 'him.\nDo', 'you', 'consent', 'we', 'shall', 'acquaint', 'him', 'with', 'it,\nAs', 'needful', 'in', 'our', 'loves,', 'fitting', 'our', "duty?\nMARCELLUS\nLet's", "do't,", 'I', 'pray;', 'and', 'I', 'this', 'morning', 'know\nWhere', 'we', 'shall', 'find', 'him', 'most', 'conveniently.\nExeunt']
"""